# -*- coding: utf-8 -*-
import shutil
from pathlib import Path
import subprocess
from itertools import takewhile


def main():
    content = Path(__file__).parent / 'content'
    pdfcontent = Path(__file__).parent / 'pdf/content/'
    pdfoutput = Path(__file__).parent / 'pdf/output/'

    pdfcontent.mkdir(parents=True)
    pdfoutput.mkdir(parents=True)

    for article in content.iterdir():
        shutil.copy(str(article), str(pdfcontent / article.name))

    for article in pdfcontent.iterdir():
        with article.open('r') as f:
            header = ''.join(takewhile(lambda x: x != '\n', f))
            text = '---\n' + header + '---\n\n' + f.read()

        with article.open('w') as f:
            f.write(text)

        subprocess.call(["pandoc", str(article), "-o",
                         "pdf/output/{}.pdf".format(article.stem)])


if __name__ == '__main__':
    main()
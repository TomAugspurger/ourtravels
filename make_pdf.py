# -*- coding: utf-8 -*-
import shutil
from pathlib import Path
import subprocess
from itertools import takewhile


def main():
    content = Path(__file__).parent / 'content'
    pdfcontent = Path(__file__).parent / 'pdf/content/'
    pdfoutput = Path(__file__).parent / 'pdf/output/'

    for f in [pdfcontent, pdfoutput]:
        try:
            f.mkdir(parents=True)
        except FileExistsError:
            pass

    for article in content.iterdir():
        shutil.copy(str(article), str(pdfcontent / article.name))

    dates = []

    for article in pdfcontent.iterdir():
        with article.open('r') as f:
            header = ''.join(takewhile(lambda x: x != '\n', f))
            d = [x for x in header.split('\n') if x[:4] == 'date'][0][-10:]
            dates.append((article.stem, d))
            text = '---\n' + header + '---\n\n' + f.read()

        with article.open('w') as f:
            f.write(text)

        subprocess.call(["pandoc", str(article), "-o",
                         "pdf/output/{}.pdf".format(article.stem)])
    dates = sorted(dates, key=lambda x: x[1])
    subprocess.call(["pdfjam", "-o", "pdf/output/book.pdf"]
                    + ["pdf/output/{}.pdf".format(x[0]) for x in dates])

if __name__ == '__main__':
    main()

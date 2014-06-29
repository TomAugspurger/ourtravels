heroku apps:delete ourtravels --confirm
heroku apps:create ourtravels
heroku config:set BUILDPACK_URL=https://github.com/getpelican/heroku-buildpack-pelican
git push heroku master
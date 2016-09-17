heroku apps:delete ourtravels --confirm ourtravels
heroku apps:create ourtravels
heroku config:set BUILDPACK_URL=https://github.com/getpelican/heroku-buildpack-pelican --app=ourtravels
git push heroku master

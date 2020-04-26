# Redis-with-geospatial-data

In this python file "code.py", you can find a basic handle of geospatial data in redis database.

We add cities with geospatial coordinates in Redis, using GEOADD function (for geospatial data...).

With GEORADIUSBYMEMBER you can get all the cities around a given city, with a given radius ! It's useful and easy to use !
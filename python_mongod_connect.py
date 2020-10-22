from pymongo import MongoClient

if None not in (userMongo, passwordMongo):
    uri = 'mongodb://{0}:{1}@{2}:{3}/?authSource=admin&readPreference=primary' \
          '&appname=MongoDB%20Compass%20Community&ssl=false' \
        .format(userMongo, passwordMongo, hostMongo, portMongo)
else:
    uri = 'mongodb://{0}:{1}/?authSource=admin&readPreference=primary&appname' \
          '=MongoDB%20Compass%20Community&ssl=false' \
        .format(hostMongo, portMongo)

conn_mongodb = MongoClient(uri)
db = client.avy
import pymongo



client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_info = ganji['ganji_url']

# for i in ganji_info.find():
#     print(i)
print(ganji_info.find().count())


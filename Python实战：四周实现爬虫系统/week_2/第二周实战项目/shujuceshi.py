import pymongo



client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_info = ganji['ganji_info']

for i in ganji_info.find():
    print(i)


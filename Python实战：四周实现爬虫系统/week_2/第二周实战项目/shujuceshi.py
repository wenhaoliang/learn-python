import pymongo



client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_data = ganji['ganjin_data']

for i in ganji_data.find():
    print(i)
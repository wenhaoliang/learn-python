import pymongo



client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_info = ganji['ganji_url']

num = 0
for i in ganji_info.find():
    if "zhuanzhuan" in i["url"]:
        num += 1
        print(num, i["url"])

import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_ta = walden['sheet_ta']

path = 'walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             '序列':index,
#             '句子' :line,
#             '单词数量':len(line.split())
#         }
#         sheet_ta.insert_one(data)

# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
for item in sheet_ta.find():
    print(item)

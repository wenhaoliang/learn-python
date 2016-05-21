import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("localhost", 27017)
xiaozhu = client['xiaozhu']
duanzu_tab = xiaozhu['duanzu_tab']

def get_info():
    #http://bj.xiaozhu.com/search-duanzufang-p1-0/
    base_url = 'http://bj.xiaozhu.com/search-duanzufang-p'
    for i in range(1,4):
        full_url = base_url + str(i) + '-0/'
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        titles = soup.select('span.result_title')
        prices = soup.select('span.result_price > i ')
        #print(titles,prices)
        for title, price in zip(titles, prices):
            data = {
                '房屋名字': title.get_text(),
                '价格'    : int(price.get_text())
            }
            duanzu_tab.insert_one(data)
            #print(data)
if __name__ == "__main__":
    get_info()
    # $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
    for item in duanzu_tab.find():
        if item['价格'] >= 500:
            print(item)



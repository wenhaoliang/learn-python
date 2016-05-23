from bs4 import BeautifulSoup
import requests
import pymongo
import time
from get_pages import urls

client = pymongo.MongoClient('localhost',27017)
neirong = client['neirong']
xinxi = neirong['xinxi']

def get_pages_from(channel,pages,who_shells='o'):
    pages_url = []
    list_view = '{}/{}{}'.format(channel,str(who_shells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if wb_data.status_code == 200:
        for link in soup.select('li.js-item a.ft-tit'):
            item_link = link.get('href')
            pages_url.append(item_link)
    else:
        pass
    print(pages_url)



#假设列表是urls
for i in range(1,100):
    for url in urls:
        get_pages_from(url,i)


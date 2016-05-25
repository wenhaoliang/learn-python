import pymongo
import requests
from bs4 import BeautifulSoup


client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_data = ganji['ganji_data']


def get_pages(base_url):
    pages_url = []
    #http://zz.ganji.com/xuniwupin/o2/
    for i in range(1,101):
        full_url = base_url + 'o{}'.format(str(i))
        wb_data = requests.get(full_url)
        if wb_data.status_code == 200:
            soup = BeautifulSoup(wb_data.text,'lxml')
            pages = soup.select('a.ft-tit')
            for page in pages:
                page = page.get('href')
                pages_url.append(page)
                # for i in pages_url:
                #     print(len(i))
    print('本次一共获取到',len(pages_url),'个页面哦')
    return pages_url



def get_pages_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('h1.title-name')
    times = soup.select('i.pr-5')
    types = soup.select('ul.det-infor > li:nth-of-type(1) > span')
    prices = soup.select('i.f22.fc-orange.f-type')
    places = soup.select("ul.det-infor > li > a")
    for titles, times,types,prices,places in zip(titles,times,types,prices,places):
        data = {
            '标题': titles.get_text(),
            '发布时间': times.get_text().strip().split(' ')[0] if len(times) > 0 else "",
            '类型' : types.get_text(),
            '价格' : prices.get_text(),
            '交易地点':places.get_text()
        }
        ganji_data.insert_one(data)


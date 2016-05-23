import requests
from bs4 import BeautifulSoup


def get_url_from():
    base_url = 'http://zz.ganji.com/wu'
    wb_data = requests.get(base_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    url = soup.select('#wrapper > div.content > div > div > dl > dt > a')
    urls = []
    for url in url:
        url  = url.get('href')
        full_url = 'http://zz.ganji.com' + url
        urls.append(full_url)
    return urls


urls = [
     'http://zz.ganji.com/jiaju/',
     'http://zz.ganji.com/rirongbaihuo/',
     'http://zz.ganji.com/shouji/',
     'http://zz.ganji.com/shoujihaoma/',
     'http://zz.ganji.com/bangong/',
     'http://zz.ganji.com/nongyongpin/',
     'http://zz.ganji.com/jiadian/',
     'http://zz.ganji.com/ershoubijibendiannao/',
     'http://zz.ganji.com/ruanjiantushu/',
     'http://zz.ganji.com/yingyouyunfu/',
     'http://zz.ganji.com/diannao/',
     'http://zz.ganji.com/xianzhilipin/',
     'http://zz.ganji.com/fushixiaobaxuemao/',
     'http://zz.ganji.com/meironghuazhuang/',
     'http://zz.ganji.com/shuma/',
     'http://zz.ganji.com/laonianyongpin/',
     'http://zz.ganji.com/xuniwupin/',
     'http://zz.ganji.com/qitawupin/',
     'http://zz.ganji.com/ershoufree/',
     'http://zz.ganji.com/wupinjiaohuan/'
]



from bs4 import BeautifulSoup
import requests

url = 'http://bj.ganji.com/wu'
host_url = 'http://bj.ganji.com'

def get_links(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#wrapper > div.content > div > div > dl > dd > a')
    for link in links:
        link = host_url + link.get('href')

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
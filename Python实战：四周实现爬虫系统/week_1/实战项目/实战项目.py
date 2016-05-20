#coding: utf-8

import urllib
import requests
from bs4 import BeautifulSoup

def get_source():
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    }

    base_url = 'http://zz.58.com/pbdn/pn'

    for i in range(1,3):
        full_url = base_url + str(i)
        wb_data = requests.get(full_url,headers = headers)
        soup = BeautifulSoup(wb_data.text,'html5lib')
        infos_url = []
        infos = soup.select(' tbody > tr > td.t > a.t')
        # infolist > table:nth-child(4) > tbody > tr > td.t > a.t
        # infolist > table:nth-child(8) > tbody > tr > td.t > a.t
        for info in infos:
            info_href = info.get('href')
            infos_url.append(info_href)
            #print(infos_url)
    return infos_url

def get_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'html5lib')

    times = soup.select('li.time')
    prices = soup.select('span.price')


    for   time, price in zip(times, prices):
        data = {
            'title' : soup.title.text,
            'time'  : time.get_text(),
            'price' : price.get_text(),
        }
        print(data)
for url in get_source():
    get_info(url)

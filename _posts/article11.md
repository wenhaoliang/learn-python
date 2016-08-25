---
title: '【四周实现爬虫系统】【第一周】第一周实战项目 '
date: 2016-05-20 16:42:52
tags: Python
---
记录自己学习这个教程的点点滴滴！
![第一周实战项目][1]
<!--more-->
代码：
    #coding: utf-8
    
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

github地址：[第一周实战项目][2]


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E4%B8%80%E5%91%A8%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE.png
  [2]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_1/%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE
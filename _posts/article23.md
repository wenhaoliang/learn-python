---
title: '【四周实现爬虫系统】【第二周】第二节练习项目：爬取手机号  '
date: 2016-05-21 13:23:14
tags: Python
---
决定在这里开个记录自己学这个教程的记录贴！
![【第二周】第二节练习项目：爬取手机号][1]
<!--more-->
代码：

    import requests
    from bs4 import BeautifulSoup
    import pymongo
    import time
    client = pymongo.MongoClient("localhost", 27017)
    tongcheng = client['tongcheng']
    tel_num = tongcheng['tel_num']
    
    def get_tel_num():
        base_url = 'http://zz.58.com/shoujihao/pn{}/'
        for pages in range(1,100):
            full_url = base_url.format(str(pages))
            time.sleep(2)
            wb_data = requests.get(full_url)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            titles = soup.select('strong.number')
            hrefs = soup.select('a.t')
            for title,href in zip(titles, hrefs):
                data = {
                    '手机号': title.get_text(),
                    '链接'  : href.get('href')
                }
                tel_num.insert_one(data)
                print(data)
    
    
    
    get_tel_num()
github地址：[【第二周】第二节练习项目：爬取手机号][2]


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E4%BA%8C%E8%8A%82%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A%E7%88%AC%E5%8F%96%E6%89%8B%E6%9C%BA%E5%8F%B7.png
  [2]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_2/2_2
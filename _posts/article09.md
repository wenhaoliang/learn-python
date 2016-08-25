---
title: '【四周实现爬虫系统】【第二周】第一节练习项目：在 MongoDB 中筛选房源 '
date: 2016-05-21 10:32:48
tags: Python
---
记录自己学习这个教程的点点滴滴！
![【第二周】第一节练习项目：在 MongoDB 中筛选房源][1]
<!--more-->
代码：

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
    
github地址：[【第二周】第一节练习项目：在 MongoDB 中筛选房源][2]


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E3%80%90%E7%AC%AC%E4%BA%8C%E5%91%A8%E3%80%91%E7%AC%AC%E4%B8%80%E8%8A%82%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A%E5%9C%A8%20MongoDB%20%E4%B8%AD%E7%AD%9B%E9%80%89%E6%88%BF%E6%BA%90.png
  [2]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_2/2_1
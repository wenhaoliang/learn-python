---
title: '【四周实现爬虫系统】【第二周】第二周实战项目  '
date: 2016-05-21 19:14:13
tags: Python
---
记录自己学习这个教程的点点滴滴！
![此处输入图片的描述][1]
<!--more-->
代码：
#channel_extracing.py

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
    
    
    # urls = [
    #      'http://zz.ganji.com/jiaju/',
    #      'http://zz.ganji.com/rirongbaihuo/',
    #      'http://zz.ganji.com/shouji/',
    #      'http://zz.ganji.com/shoujihaoma/',
    #      'http://zz.ganji.com/bangong/',
    #      'http://zz.ganji.com/nongyongpin/',
    #      'http://zz.ganji.com/jiadian/',
    #      'http://zz.ganji.com/ershoubijibendiannao/',
    #      'http://zz.ganji.com/ruanjiantushu/',
    #      'http://zz.ganji.com/yingyouyunfu/',
    #      'http://zz.ganji.com/diannao/',
    #      'http://zz.ganji.com/xianzhilipin/',
    #      'http://zz.ganji.com/fushixiaobaxuemao/',
    #      'http://zz.ganji.com/meironghuazhuang/',
    #      'http://zz.ganji.com/shuma/',
    #      'http://zz.ganji.com/laonianyongpin/',
    #      'http://zz.ganji.com/xuniwupin/',
    #      'http://zz.ganji.com/qitawupin/',
    #      'http://zz.ganji.com/ershoufree/',
    #      'http://zz.ganji.com/wupinjiaohuan/'
    # ]
    #
    #

#page_parsing.py

    import pymongo
    import requests
    from bs4 import BeautifulSoup
    
    
    client = pymongo.MongoClient('localhost', 27017)
    ganji = client['ganji']
    ganji_data = ganji['ganjin_data']
    
    
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


#main.py

    import time
    from multiprocessing import Pool
    from channel_extracing import get_url_from
    from page_parsing import get_pages, get_pages_info
    import time
    
    
    # def get_pages_urls():
    #     urls = get_url_from()
    #     pages_urls = []
    #     for i in range(0, len(urls)):
    #         page = get_pages(urls[i])
    #         pages_urls.append(page)
    #     for j in range(0,len(pages_urls)):
    #         get_pages_info(pages_urls[j])
    
    if __name__ == '__main__':
        urls = get_url_from()
        pages_urls = []
        for i in range(0, len(urls)):
            time.sleep(2)
            page = get_pages(urls[i])
            pages_urls.append(page)
            print(pages_urls)
        # pool = Pool()
        # pool = get_pages_urls()
        # pool.close()
        # pool.join()
        #get_pages_urls()
    
    
github地址：[第二周实战项目][2]
    


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E4%BA%8C%E5%91%A8%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE.png
  [2]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_2/%E7%AC%AC%E4%BA%8C%E5%91%A8%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE
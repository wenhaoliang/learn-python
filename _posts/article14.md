---
title: '【四周实现爬虫系统】【第一周】第四节练习项目：爬取霉霉图片 '
date: 2016-05-20 10:47:31
tags: Python
---
记录自己学习这个教程的点点滴滴！
完成了爬取图片的练习，并学到了split 与urlretrieve以及requests.get如何使用ip代理

![第四节练习项目：爬取霉霉图片][1]
<!--more-->
![第四节练习项目：爬取霉霉图片_结果][2]
![requests.get用法][3]
    #coding:utf-8
    import urllib
    import requests
    from bs4 import BeautifulSoup
    
    base_url = 'http://weheartit.com/inspirations/beach?page='
    path = 'H:\图片\四周\ '
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
    }
    # 此网站会有针对 ip 的反爬取，可以采用代理的方式
    proxies = {"http": "http://121.69.29.153:8118"}
    
    def get_url(num):
        img_urls = []
        for i in range(1, num+1):
            fullurl = base_url + str(i)
            wb_data = requests.get(fullurl, proxies)
            soup = BeautifulSoup(wb_data.text, 'html5lib')
            img_url = soup.select('img.entry_thumbnail')
    
            for j in img_url:
                img_urls.append(j.get('src'))
    
        print((len(img_urls)), '张图片需要被下载')
        return img_urls
    
    
    # 'http://data.whicdn.com/images/224263340/superthumb.jpg'
    def dl_img(url):
        urllib.request.urlretrieve(url, path + url.split("/")[-2] + url.split("/")[-1])
        '''
        url = 'http://data.whicdn.com/images/224263340/superthumb.jpg'
        >>> url.split('/')[-2]
        '224263340'
        >>> url.split('/')[-1]
        'superthumb.jpg'
        '''
        '''
        urllib.urlretrieve(url[, filename[, reporthook[, data]]])
        参数说明：
        url：外部或者本地url
        filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
        reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
        data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。
        '''
    for url in get_url(11):
        dl_img(url)
github地址：[第四节练习项目：爬取霉霉图片][4]


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E5%9B%9B%E8%8A%82%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A%E7%88%AC%E5%8F%96%E9%9C%89%E9%9C%89%E5%9B%BE%E7%89%87.png
  [2]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E5%9B%9B%E8%8A%82%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A%E7%88%AC%E5%8F%96%E9%9C%89%E9%9C%89%E5%9B%BE%E7%89%87_%E7%BB%93%E6%9E%9C.png
  [3]: http://7xtji5.com1.z0.glb.clouddn.com/%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95%20%E2%80%94%20Requests%201.1.0%20%E6%96%87%E6%A1%A3.jpg
  [4]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_1/1_4
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

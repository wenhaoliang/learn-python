import requests
from bs4 import BeautifulSoup
import urllib.request

# 'http://weheartit.com/inspirations/beach?page=8' full url

base_url = 'http://weheartit.com/inspirations/beach?page='
path = 'H:\图片\四周\ '
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}

proxies = {"http": "http://121.69.29.153:8118"}

# 此网站会有针对 ip 的反爬取，可以采用代理的方式

def get_image_url(num):
    img_urls = []
    for page_num in range(1,num+1):
        full_url = base_url + str(page_num)
        wb_data  = requests.get(full_url,proxies)
        soup = BeautifulSoup(wb_data.text,'html5lib')
        imgs = soup.select('img.entry_thumbnail')

        for i in imgs :
            img_urls.append(i.get('src'))

    print((len(img_urls)),'images shall be downloaded!')
    return img_urls

# get_image_url(1)

# 'http://data.whicdn.com/images/224263340/superthumb.jpg'
def dl_image(url):
    urllib.request.urlretrieve(url,path + url.split('/')[-2] + url.split('/')[-1])#split('')去除''中的字符
    '''
    urllib.urlretrieve(url[, filename[, reporthook[, data]]])
    参数说明：
    url：外部或者本地url
    filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
    reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
    data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。
    '''
    print('Done')

#
for url in get_image_url(10):
    dl_image(url)

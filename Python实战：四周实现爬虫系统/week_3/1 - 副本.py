from bs4 import BeautifulSoup
path = './index.html'  #这里使用了相对路径,只要你本地有这个文件就能打开

with open(path, 'r') as wb_data: # 使用with open打开本地文件
    Soup = BeautifulSoup(wb_data, 'lxml') # 解析网页内容
    #print(Soup)
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    print(images)


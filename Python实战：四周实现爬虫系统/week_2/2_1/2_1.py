import requests
from bs4 import BeautifulSoup

def get_info():
    #http://bj.xiaozhu.com/search-duanzufang-p1-0/
    base_url = 'http://bj.xiaozhu.com/search-duanzufang-p'
    for i in range(1,4):
        full_url = base_url + str(i) + '-0/'
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'html5lib')
        title = soup.select('span.result_title')
get_info()
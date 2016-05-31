import time
from multiprocessing import Pool
import multiprocessing
from page_parsing import get_pages, get_pages_info,ganji_url,ganji_data1

urls = [
    'http://zz.ganji.com/jiaju/',
    'http://zz.ganji.com/rirongbaihuo/',
    'http://zz.ganji.com/shouji/',
    'http://zz.ganji.com/shoujihaoma/',
    'http://zz.ganji.com/bangong/',
    'http://zz.ganji.com/nongyongpin/',
    'http://zz.ganji.com/jiadian/',
    'http://zz.ganji.com/ershoubijibendiannao/',
    'http://zz.ganji.com/ruanjiantushu/',
    'http://zz.ganji.com/yingyouyunfu/',
    'http://zz.ganji.com/diannao/',
    'http://zz.ganji.com/xianzhilipin/',
    'http://zz.ganji.com/fushixiaobaxuemao/',
    'http://zz.ganji.com/meironghuazhuang/',
    'http://zz.ganji.com/shuma/',
    'http://zz.ganji.com/laonianyongpin/',
    'http://zz.ganji.com/xuniwupin/',
    'http://zz.ganji.com/qitawupin/',
    'http://zz.ganji.com/ershoufree/',
    'http://zz.ganji.com/wupinjiaohuan/'
]
# def get_pages_():
#     db_urls = [item['url'] for item in ganji_url.find()]
#     index_urls = [item['url'] for item in ganji_data1.find()]
#     x = set(db_urls)
#     y = set(index_urls)
#     rest_of_urls = x - y
#     for page in rest_of_urls:
#         get_pages_info(page)
        # time.sleep(2)

if __name__ == '__main__':
    while True:
        print(ganji_data1.find().count())
        a = ganji_data1.find().count()
        time.sleep(3)
        b = ganji_data1.find().count()
        print(b - a)
    db_urls = [item['url'] for item in ganji_url.find()]
    index_urls = [item['url'] for item in ganji_data1.find()]
    x = set(db_urls)
    y = set(index_urls)
    rest_of_urls = x - y
    rest_of_urls = list(rest_of_urls)
    pool = Pool()
    for i in range(len(rest_of_urls)):
        pool.apply_async(get_pages_info, args=(rest_of_urls[i],))
    pool.close()
    pool.join()





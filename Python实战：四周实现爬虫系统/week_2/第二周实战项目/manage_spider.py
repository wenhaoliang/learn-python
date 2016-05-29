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
    db_urls = [item['url'] for item in ganji_url.find()]
    index_urls = [item['url'] for item in ganji_data1.find()]
    x = set(db_urls)
    y = set(index_urls)
    rest_of_urls = x - y
    pool = Pool()
    pool.map(get_pages_info, rest_of_urls)
    pool.close()
    pool.join()





    # pool = Pool()
    # for i in range(4):
    #     pr = multiprocessing.Process(target=get_pages_())
    #     pr.close()
    #     pr.join()
    # pool.close()
    # pool.join()
    # process1 = multiprocessing.Process(target=get_pages(), args=(urls,))
    # process1.start()
    # process1.join()
    # process2 = multiprocessing.Process(target= get_pages_)
    # process2.start()
    # process2.join()
    # #process1.close()
    # process2.close()





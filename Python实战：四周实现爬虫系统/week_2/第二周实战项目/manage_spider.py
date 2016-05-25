import time
from multiprocessing import Pool
from channel_extracing import get_url_from
from page_parsing import get_pages, get_pages_info



# def get_pages_urls():
#     urls = get_url_from()
#     pages_urls = []
#     for i in range(0, len(urls)):
#         page = get_pages(urls[i])
#         pages_urls.append(page)
#     for j in range(0,len(pages_urls)):
#         get_pages_info(pages_urls[j])

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
def get_pages_(url):
    page = get_pages(url)
    for pages_url in page:
        get_pages_info(pages_url)

if __name__ == '__main__':

    # urls = get_url_from()
    # pages_urls = []
    # for i in range(0, len(urls)):
    #     # time.sleep(2)
    #     page = get_pages(urls[i])
    #     print(page)
        # pages_urls.append(page)
        # print(pages_urls)
    pool = Pool()
    pool.map(get_pages_,urls)
    pool.close()
    pool.join()
    #get_pages_urls()





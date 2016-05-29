import time
from multiprocessing import Pool
from page_parsing import get_pages, get_pages_info

urls = [
    # 'http://zz.ganji.com/jiaju/',
    # 'http://zz.ganji.com/rirongbaihuo/',
    # 'http://zz.ganji.com/shouji/',
    # 'http://zz.ganji.com/shoujihaoma/',
    # 'http://zz.ganji.com/bangong/',
    # 'http://zz.ganji.com/nongyongpin/',
    # 'http://zz.ganji.com/jiadian/',
    # 'http://zz.ganji.com/ershoubijibendiannao/',
    # 'http://zz.ganji.com/ruanjiantushu/',
    # 'http://zz.ganji.com/yingyouyunfu/',
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
        #time.sleep(2)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_pages_,urls)
    pool.close()
    pool.join()





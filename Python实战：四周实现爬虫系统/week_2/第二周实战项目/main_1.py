
from multiprocessing import Pool
from channel_extracing import get_url_from
from page_parsing import get_pages, get_pages_info





if __name__ == '__main__':
    pool = Pool()
    urls = get_url_from()
    get_pages_urls = map(get_pages,urls)
    pool.map(get_pages_info, list(get_pages_urls))
    pool.close()
    pool.join()



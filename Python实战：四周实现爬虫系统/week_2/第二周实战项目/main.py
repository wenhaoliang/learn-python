import time
from multiprocessing import Pool
from channel_extracing import get_url_from
from page_parsing import get_pages, get_pages_info
import time


# def get_pages_urls():
#     urls = get_url_from()
#     pages_urls = []
#     for i in range(0, len(urls)):
#         page = get_pages(urls[i])
#         pages_urls.append(page)
#     for j in range(0,len(pages_urls)):
#         get_pages_info(pages_urls[j])

if __name__ == '__main__':
    urls = get_url_from()
    pages_urls = []
    for i in range(0, len(urls)):
        time.sleep(2)
        page = get_pages(urls[i])
        pages_urls.append(page)
        print(pages_urls)
    # pool = Pool()
    # pool = get_pages_urls()
    # pool.close()
    # pool.join()
    #get_pages_urls()





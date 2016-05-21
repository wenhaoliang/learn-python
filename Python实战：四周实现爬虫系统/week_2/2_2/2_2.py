    import requests
    from bs4 import BeautifulSoup
    import pymongo
    import time
    client = pymongo.MongoClient("localhost", 27017)
    tongcheng = client['tongcheng']
    tel_num = tongcheng['tel_num']

    def get_tel_num():
        base_url = 'http://zz.58.com/shoujihao/pn{}/'
        for pages in range(1,100):
            full_url = base_url.format(str(pages))
            time.sleep(2)
            wb_data = requests.get(full_url)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            titles = soup.select('strong.number')
            hrefs = soup.select('a.t')
            for title,href in zip(titles, hrefs):
                data = {
                    '手机号': title.get_text(),
                    '链接'  : href.get('href')
                }
                tel_num.insert_one(data)
                print(data)



    get_tel_num()
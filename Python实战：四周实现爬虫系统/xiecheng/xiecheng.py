#conding:utf-8

import requests
from bs4 import BeautifulSoup
from ghost import Ghost

from ghost import Ghost, Session

gh = Ghost()

se = Session(gh, display = True)

se.open("https://www.liangwenhao.cn/")

# import ghost
#
# g = ghost.Ghost()
# with g.start() as session:
#     page, extra_resources = session.open("https://www.debian.org")
#     if page.http_status == 200 and \
#             'The Universal Operating System' in page.content:
#         print("Good!")
# import json
# # import urllib2
#
# url = 'http://flights.ctrip.com/international/round-zhengzhou-macau-cgo-mfm?2016-05-25&2016-06-22&y'
#
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# airline_name = soup.select('#arrivalCity')
# for i in airline_name:
#     i = i.get_text()
#     print(i)
# print(soup)


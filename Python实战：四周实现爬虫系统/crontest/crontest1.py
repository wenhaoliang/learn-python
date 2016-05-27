import requests
from bs4 import BeautifulSoup

headers = {
    'cookie' : 'd_c0="AJDA7uPq0AmPTqVQBZlvJv-fgF5mjXZdzjI=|1461419041"; _zap=bbc6e7cc-6f6f-49cc-b6a3-a066f5656c9b; _za=e8101019-3138-4c31-8a2d-3a507fe0c46f; l_cap_id="YmZlNTcwMWI4N2M5NDcxMzhhNzgyN2RkYjBjMjJlMGM=|1462336507|8c2ae7baeae45942abbe49dab6abf924a8ae061d"; cap_id="YWFjOTkyNTI4MzlmNDUzZWE1Yjg4N2UyZjVhMWZmZjM=|1462336507|4562e75b108451bee7f820343228fcd0a48454b5"; z_c0=Mi4wQUJBTS1ILXptQWdBa01EdTQtclFDUmNBQUFCaEFsVk5EQWxSVndDVVA1bmxWSG1vU0d4aHE4cy1OV2ROLU5fRlB3|1462336524|e62204dce3416191c1344971059047a662af6d20; _ga=GA1.2.1774971702.1462978329; q_c1=025a9fc27da240a3a0ac1b6ce7a36a09|1464062348000|1461419039000; _xsrf=5b538c4d17c5159e68a5e1693fe624d8; __utmt=1; __utma=51854390.1774971702.1462978329.1464063175.1464274292.5; __utmb=51854390.2.10.1464274292; __utmc=51854390; __utmz=51854390.1463969158.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20150825=1^3=entry_date=20150825=1'

}
url = 'https://www.zhihu.com/#signin'
wb_data = requests.get(url,headers = headers)
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('a.question_link')
text = soup.select('#feed-0 > div.feed-item-inner > div.feed-main > div.feed-content.zm-item-expanded > div.expandable.entry-body > div.zm-item-rich-text.expandable.js-collapse-body > div:nth-child(1)')
for title in text:
    title = title.get_text()
    print(title)

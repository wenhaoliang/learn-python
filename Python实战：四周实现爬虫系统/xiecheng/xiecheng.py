#conding:utf-8

import requests
from bs4 import BeautifulSoup


url = 'http://flights.ctrip.com/international/AjaxRequest/SearchFlights/AsyncSearchResultHandler.ashx'
headers = {
    'Accept'          :'*/*',
    'Accept-Encoding' :'gzip, deflate',
    'Accept-Language' :'zh-CN,zh;q=0.8',
    'Cache-Control'   :'-age=0',
    'Connection'      :'keep-alive',
    'Content-Length'  :'1431',
    'Content-Type'    :'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie'          :'_abtest_userid=3cc30bda-ffa7-4dbf-a4fd-982ca2cbdd37; adscityen=Zhengzhou; Session=smartlinkcode=U130678&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4899&SID=130678&OUID=; Customer=HAL=ctrip_gb; appFloatCnt=2; manualclose=1; ASP.NET_SessionSvc=MTAuMTUuMTM2LjMxfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTQ0ODk1ODg2OTAyOQ; _bfa=1.1463895447080.4ddz23.1.1463895447080.1463902033579.2.8; _bfs=1.2; FlightIntl=Search=%5B%22Zhengzhou%7C%E9%83%91%E5%B7%9E(CGO)%7C559%7CCGO%7C480%22%2C%22Macau%7C%E6%BE%B3%E9%97%A8(MFM)%7C59%7CMFM%7C480%22%2C%222016-05-25%22%2C%222016-06-22%22%5D; __zpspc=9.2.1463902036.1463902268.2%233%7Cwww.google.com.hk%7C%7C%7C%7C%23; _ga=GA1.2.151454271.1463895455; _jzqco=%7C%7C%7C%7C1463895462491%7C1.843687252.1463895455840.1463902036314.1463902267990.1463902036314.1463902267990.undefined.0.0.8.8; _bfi=p1%3D104003%26p2%3D104003%26v1%3D8%26v2%3D7',
    'Host'            :'flights.ctrip.com',
    'Origin'          :'http://flights.ctrip.com',
    'Referer'         :'http://flights.ctrip.com/international/round-zhengzhou-macau-cgo-mfm?2016-05-25&2016-06-22&y',
    'User-Agent'      :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
}
data = {
    'SearchMode'     : 'TokenSearch',
    'condition'      : '{"FlightWay":"D","SegmentList":[{"DCityCode":"CGO","ACityCode":"MFM","DCity":"Zhengzhou|郑州(CGO)|559|CGO|480","ACity":"Macau|澳门(MFM)|59|MFM|480","DepartDate":"2016-5-25"},{"DCityCode":"MFM","ACityCode":"CGO","DCity":"Macau|澳门(MFM)|59|MFM|480","ACity":"Zhengzhou|郑州(CGO)|559|CGO|480","DepartDate":"2016-6-22"}],"TransferCityID":0,"Quantity":1,"TransNo":"4716052215000079053","SearchRandomKey":"","IsAsync":1,"RecommendedFlightSwitch":1,"EngineFlightSwitch":1,"SearchKey":"2DB3F5A90AAFCD071ED7BD675CD80906AA0A070AA4BE02EA3AED6D4A7E75789C203842AD5B68145AA98DF39C286DC22D82BEE57CE15A7AB7","MultiPriceUnitSwitch":1,"TransferCitySwitch":false,"EngineFlightFltNo":"D","EngineFlightRT":"C","EngineABTesting2":"B","SearchStrategySwitch":1,"MaxSearchCount":3,"TicketRemarkSwitch":1,"RowNum":"1500","TicketRemarkChannels":["GDS-WS","ZY-WS"],"AddSearchLogOneByOne":true,"TFAirlineQTE":"AA","IsWifiPackage":',
    'DisplayMode'    : 'RoundTripGroup',
    'SearchToken'    : '3'
}

wb_data = requests.post(url, data = data )
soup = BeautifulSoup(wb_data.text,'lxml')
airline_name = soup.select('#arrivalCity')
for i in airline_name:
    i = i.get_text()
    print(i)
print(soup)


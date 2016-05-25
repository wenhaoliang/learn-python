#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pymongo
import time
from page_parsing import ganji_data
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_info = ganji['ganji_info']

while True:
    print(ganji_info.find().count())
    time.sleep(3)

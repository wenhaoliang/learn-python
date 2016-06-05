#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
ganji_data1 = ganji['ganji_data3']
ganji_url = ganji['ganji_url']


while True:
    print(ganji_data1.find().count())
    print("-" * 100)
    a = ganji_data1.find().count()
    time.sleep(3)
    b = ganji_data1.find().count()
    print(b-a)
    print("-" * 100)
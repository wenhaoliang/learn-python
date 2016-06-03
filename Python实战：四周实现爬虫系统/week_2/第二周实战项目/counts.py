#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from page_parsing import ganji_data2,ganji_url

while True:
    print(ganji_data2.find().count())
    print("-"*100)
    a = ganji_data2.find().count()
    time.sleep(3)
    b = ganji_data2.find().count()
    print(b-a)
    print("-" * 100)
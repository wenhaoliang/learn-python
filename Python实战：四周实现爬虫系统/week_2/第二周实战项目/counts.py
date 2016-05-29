#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from page_parsing import ganji_data1,ganji_url

while True:
    print(ganji_data1.find().count())
    a = ganji_data1.find().count()
    time.sleep(3)
    b = ganji_data1.find().count()
    print(b-a)
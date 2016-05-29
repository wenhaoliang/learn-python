#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from page_parsing import ganji_data

while True:
    print(ganji_data.find().count())
    a = ganji_data.find().count()
    time.sleep(3)
    b = ganji_data.find().count()
    print(b - a)

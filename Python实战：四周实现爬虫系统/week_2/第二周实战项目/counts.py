#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from page_parsing import ganjin_data

while True:
    print(ganjin_data.find().count())
    time.sleep(3)

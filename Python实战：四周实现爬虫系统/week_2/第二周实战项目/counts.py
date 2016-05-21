#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from page_parsing import ganji

while True:
    print(ganji.find().count())
    time.sleep(5)

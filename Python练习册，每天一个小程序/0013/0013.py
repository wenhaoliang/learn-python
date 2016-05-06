# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0013 题： 用 Python 写一个爬图片的程序
from tools import geturlimgs

def get_url_imgs(url=None):
    if url is None:
        return None

    tmp = geturlimgs.geturlimgs()
    tmp.get_imgs(url, "/Users/xieyajie/Desktop/Python/ShowMeCode/xyjxyf/0013/")
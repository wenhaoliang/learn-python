# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 北京, 程序员, 公务员, 领导, 牛比, 牛逼, 你娘, 你妈, love, sex, jiangge
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def find_sensitive_words(sensitive_file=None, input_string=None):
    if sensitive_file is None or input_string is None:
        return None

    file = open(sensitive_file, "r")
    sensitive_words = file.read().split()

    is_sensitive = False
    for sensitive in sensitive_words:
        if sensitive in input_string:
            is_sensitive = True
            print("Freedom")

    if not is_sensitive:
        print("Human Rights")

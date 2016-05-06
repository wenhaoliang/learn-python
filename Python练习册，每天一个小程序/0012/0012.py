# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def replace_sensitive_words(sensitive_file=None, input_string=None):
    if sensitive_file is None or input_string is None:
        return None

    file = open(sensitive_file, "r")
    sensitive_words = file.read().split()

    for sensitive in sensitive_words:
        if sensitive in input_string:
            replace_str = "*" * len(sensitive)
            input_string = input_string.replace(sensitive, replace_str)

    print(input_string)
# -*- coding: utf-8 -*-
#by liangwenhao
#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count(filepath):
    f = open(filepath, 'rb')#打开文件 rb     以二进制读模式打开
    s = f.read()#读文件
    words = re.findall(r'[a-zA-Z0-9]+', s)#findall方法寻找，[a-zA-Z0-9] == [\w]
	#words = re.findall(r'[\w]+', s)
    return len(words)#返回长度

if __name__ == '__main__':
    num = count(u'英文字符.txt')
    print num

	 
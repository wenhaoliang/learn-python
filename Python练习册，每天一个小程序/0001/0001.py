# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

def rand_str(num, length = 7):
    f = open(u'激活码.txt', 'wb')#打开文件
    for i in range(num):#外圈循环
        chars = string.letters + string.digits
		#string.letters：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
		#string.digits： 0123456789
        s = [random.choice(chars) for i in range(length)]
		#random.choice(chars)是从chars中随机选出一个字符, 之后是生成length的长度
        f.write(''.join(s) + '\n')#join方法是字符串s之间用"*"中间的*连接
    f.close()#关闭文件

if __name__ == '__main__':
    rand_str(200,8)
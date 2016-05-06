# -*- coding: utf-8 -*-
#by liangwenhao
#第 0008 题：一个HTML文件，找出里面的正文。

from bs4 import BeautifulSoup

def find_the_content(path):
	with open(path) as f:#使用with比较安全
		text = BeautifulSoup(f, 'lxml')#创建bs对象
		content = text.get_text().strip('\n')#获取文字并去除换行符
		#fp = open("result.txt","w")
		fp.write("result.txt",content.encode('gbk','ignore'))#ignore忽略其中异常的编码


if __name__ == '__main__':
	print find_the_content('1.html')
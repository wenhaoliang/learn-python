# -*- coding: utf-8 -*-
#by liangwenhao
#第 0009 题：一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup
import requests

def get_links(html):
	soup = BeautifulSoup(html,"lxml")#创建bs对象
	links = []#创建列表
	for link in soup.find_all("a"):
			href = link["href"]#将找到的href标签赋值给href
			if href.startswith("http"):
				links.append(href)#将其添加到links
	fp = open("result.txt","w")#写入txt中
	for item in links:
		fp.write(item)
		fp.write("\n")
	fp.close()


if __name__ == '__main__':
	r = requests.get("https://github.com/")
	html = r.text
	links = get_links(html)

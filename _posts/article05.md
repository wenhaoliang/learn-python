---
title: '【四周实现爬虫系统】【第一周】第二节练习项目：爬取商品信息 '
date: 2016-05-18 21:50:03
tags: Python
---
记录自己学习这个教程的点点滴滴！
![第二节练习项目：爬取商品信息][1]
代码：	<!--more-->

	#-*- coding: utf-8 -*-
	from bs4 import BeautifulSoup
	#这里使用了相对路径,只要你本地有这个文件就能打开
	path = './1_2_homework_required/index.html'

	# 使用with open打开本地文件
	# 第一个参数是文件地址；第二个参数是文件处理方式：r表示读取文件;w表示写文件
	with open(path, 'r') as wb_data:
		# 解析网页内容
		soup = BeautifulSoup(wb_data, 'html5lib')

		# 复制每个元素的css selector 路径即可
		# 注意 > 两边留有空格，否则会报错；
		# 注意如果有nth-child(),需要删掉，或者替换为nth-of-type否则易报错
		titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
		images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
		reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
		prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
		stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
		# 为了从父节点开始取,此处保留:nth-of-type(2),观察网页,多取几个星星的selector,就发现规律了

		# 使用for循环,把每个元素装到字典中
		for title, image, review, price, star in zip(titles, images, reviews, prices, stars):
			data = {
				# 使用get_text()方法取出文本
				'title': title.get_text(),

				# 使用get 方法取出带有src的图片链接
				'image': image.get('src'),
				'review': review.get_text(),
				'price': price.get_text(),

				# 观察发现,每一个星星会有一次<span class="glyphicon glyphicon-star"></span>,所以我们统计有多少次,就知道有多少个星星了;
				# 使用find_all 统计有几处是★的样式,第一个参数定位标签名,第二个参数定位css 样式,具体可以参考BeautifulSoup 文档示例http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all;
				# 由于find_all()返回的结果是列表,我们再使用len()方法去计算列表中的元素个数,也就是星星的数量
				'star': len(star.find_all("span", class_='glyphicon glyphicon-star'))
			}
			print (data)

github地址：[第二节练习项目：爬取商品信息][2]
    
    


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/%E7%AC%AC%E4%BA%8C%E8%8A%82%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A%E7%88%AC%E5%8F%96%E5%95%86%E5%93%81%E4%BF%A1%E6%81%AF.png
  [2]: https://github.com/wenhaoliang/learn-python/tree/master/Python%E5%AE%9E%E6%88%98%EF%BC%9A%E5%9B%9B%E5%91%A8%E5%AE%9E%E7%8E%B0%E7%88%AC%E8%99%AB%E7%B3%BB%E7%BB%9F/week_1/1_2
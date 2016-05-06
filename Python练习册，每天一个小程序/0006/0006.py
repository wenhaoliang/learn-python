# -*- coding: utf-8 -*-
#by liangwenhao
#第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os, re

def find_word(file_path):
	file_list = os.listdir(file_path)#获取文件
	word_dic = {}#创建列表
	word_re = re.compile(r'[\w]+')#匹配【a-zA-Z0-9】
	for x in file_list:#遍历所有文件
		if os.path.isfile(x) and os.path.splitext(x)[1] =='.txt' :#判断是否是txt文件
			try:
				f = open(x, 'r')#打开文件，以读的方式
				data = f.read()#读取
				f.close()#关闭
				words = word_re.findall(data)#匹配【a-zA-Z0-9】 
				for word in words:#遍历英文，记录每次词出现的次数
					if word not in word_dic:
						word_dic[word] = 1
					else:
						word_dic[word] += 1
			except:
				print('Open %s Error' % x)
	Ans_List = sorted(word_dic.items(), key = lambda t : t[1], reverse = True)
	#word_dic.items() 返回可遍历的(键, 值) 元组数组。
	#>>>dict = {'Name': 'Zara', 'Age': 7}
	#>>>print "Value : %s" %  dict.items()
	#>>>Value : [('Age', 7), ('Name', 'Zara')]
	#sorted(data, cmp=None, key=None, reverse=False)
	#其中，data是待排序数据，可以使List或者iterator, cmp和key都是函数，这两个函数作用与data的元素上产生一个结果，sorted方法根据这个结果来排序。 reverse = True 会改变data
	fp = open("result.txt","w")
	for key, value in Ans_List:
		fp.write('Word %s '% key )
		fp.write('appears %d times\n' % value)
	fp.close()
find_word('.')
---
title: '几个关于python的小问题'
date: 2016-08-22 13:26:35
tags: python
---
问题：
1、安装完之后，在命令行打python，提示‘python’不是内部或外部命令，也不是可运行的程序或批处理文件。
原因是什么？要如何解决？
2、city.py的内容：
```
city = {
	'北京': '101010100',
	'海淀': '101010200',
	'朝阳': '101010300',
	'顺义': '101010400',
}
```
test.py的内容：

```
from city import city 
name = raw_input() 
print city.get(name)
```

<!--more-->
test.py运行时报错
SyntaxError: Non-ASCII character '\xe5' in file /Users/qinng/Code/Python/city.py on line 2, but no encoding declared;
是什么原因？
可执行，但输入“北京”后未显示结果，是什么原因？
3、抓取某网页内容，返回[HTTP Error 403: Forbidden]可能是什么原因？要如何解决？
4、列举向文件中写入内容时，有可能犯的错误。（包括各种新手可能犯的低级错误）
5、列举python2和python3较常见不同之处。


1、没有在路径path中添加 python.exe
2、（1）、python的默认编码文件是用的ASCII码，这里使用了中文汉字，可以在开头加入# coding=UTF-8或者# -*- coding:UTF-8 -*-解决
   （2）、这个我试了试，无论在2.7或者3.5的情况下都是正常输入的，所以没办法解答这个问题啊 = = ![python2.7未添加# coding=UTF-8][1]
   ![python2.7已添加# coding=UTF-8][2]
   ![python3.5][3]
3、 验证请求信息中的UserAgent出现异常。解决方案是添加完整的个性化的UserAgent（伪装成正常的浏览器）。   
4、首先，为预防出现错误可以使用 try except进行异常处理。
（0）、未向文件头添加# coding=UTF-8，导致编码错误
（1）、python的关键字出现不起眼的错误，比如print写成pirnt
（2）、对文本读写时使用方法错误。对文本进行读取或写入字符时，要使用r或者w，要对文本文件进行读出或写入数据时，使用rb或者wb。
（3）、文本位置错误，读文件时文本的位置搞错。
5、（0）、最方便的一点就是改善了编码的问题，给初学者带来了极大的方便。
（1）print的差别，2.7是print ""
、3.5是pirnt().
（2）、原来1/2（两个整数相除）结果是0，现在是0.5了。
（3）、!=取代 < >
（4）、except Exception, e变成except (Exception) as e
（5）、在 Python 3.x 中 for 循环变量不会再导致命名空间泄漏。
（6）、python3将raw_input()改成input()，上面的图片也说明这点。


  [1]: http://7xtji5.com1.z0.glb.clouddn.com/QQ%E5%9B%BE%E7%89%8720160822131252.jpg
  [2]: http://7xtji5.com1.z0.glb.clouddn.com/QQ%E5%9B%BE%E7%89%8720160822131258.png
  [3]: http://7xtji5.com1.z0.glb.clouddn.com/QQ%E6%88%AA%E5%9B%BE20160822131557.jpg
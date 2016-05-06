# -*- coding: utf-8 -*-
#by liangwenhao
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image, ImageOps
import os, os.path

L = [ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.jpg' ] 
#os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作 
 

for x in L:
    img = Image.open(x)#创建image对象
    xsize, ysize = img.size#获取高宽
    xsize = 500#设定高
    ysize = ysize * 500 // xsize#设定宽
    img = ImageOps.fit(img,(xsize,ysize))#修改尺寸 
    img.save("out"+x)#保存
# -*- coding: utf-8 -*-
#by liangwenhao
#第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os

#获取path路径下的文件
def get_files(path):
    filepath = os.listdir(path)# # 获得path目录中的内容
    files = []#创建列表
    for fp in filepath:
        fppath = path + '/' + fp#拼接文件路径
        if(os.path.isfile(fppath)):#判断是否为文件
            files.append(fppath)#将文件添加到files中
        elif(os.path.isdir(fppath)):#判断是否为文件夹
            files += get_files(fppath)#使用一个迭代将文件夹里的文件加入到files中
    return files#返回files列表 

# 统计代码，空行与注释
def count_lines(files):
    line, blank, note = 0, 0, 0#初始化数量
    for filename in files:
        f = open(filename, 'rb')#以二进制读的方式打开
        for l in f:
            l = l.strip()#删除l中的空白符
            line += 1#记录行数
            if l == '':
                blank += 1#统计空行
            elif l[0] == '#' or l[0] == '/':#统计注释
                note += 1
        f.close()
    return (line, blank, note)

if __name__ == '__main__':
    files = get_files('.')
    print files
    lines = count_lines(files)
    print u'代码行数是: %d, 空白行数是: %d, 注释行数是: %d' % (lines[0], lines[1], lines[2])
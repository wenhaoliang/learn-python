# -*- coding: utf-8 -*-
#by liangwenhao
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)#创建图片对象
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)#设定自己的字体及其大小
    fillcolor = "#ff0001"#颜色
    width, height = img.size#获取高、宽
    draw.text((width-60, 0), '101', font=myfont, fill=fillcolor)#将101写入右上角（宽减去60，最高）处，字体与颜色替换
    img.save('result.jpg','jpeg')#保存

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image) 
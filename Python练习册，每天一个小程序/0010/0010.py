# -*- coding: utf-8 -*-
#by liangwenhao
#第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_image(image_size = (300, 100),
			   background_color = (255, 255, 0),
			   font_type = "arialbd.ttf",
			   font_size = 50,
			   text_num = 4,
			   point_chance = 50):

	im = Image.new("RGB", image_size, background_color)#创建图片对象
	draw = ImageDraw.Draw(im)#创建绘图对象
	image_width, image_height = image_size#获取高宽

	def create_text():#定义写字母函数
		text_font = ImageFont.truetype(font_type, font_size)#设定字体和大小
		font_width, font_height = text_font.getsize("A")#字体大小
		for i in range(text_num):
			text = random.choice(string.ascii_uppercase)#ABCDEFGHIJKLMNOPQRSTUVWXYZ
			text_loc = ((image_width - font_width) / text_num * (i + 0.5), (image_height - font_height) / 2.3)#不懂，标记
			draw.text(text_loc, text, font = text_font, fill = (random.randint(0, 255) / 2, random.randint(0, 255) / 2, random.randint(0, 255) / 2))
			
	def create_points():#定义画点函数
		for w in range(image_width):
			for h in range(image_height):
				tmp = random.randint(0, 100)
				if tmp > point_chance:
					draw.point((w, h), fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
	


	create_text()
	#create_points()
	im = im.filter(ImageFilter.BLUR)
	im.save("result.jpg")
	return im

if __name__ == "__main__":
	im = create_image()
	#im.show()
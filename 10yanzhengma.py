#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0010 题：使用 Python 生成类似于图中的字母验证码图片'

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random,string

# 随机字母:
def rndChar():
    chars = string.digits + string.ascii_letters
    s = [random.choice(chars) for i in range(4)]
    return ''.join(s)

    #return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))#一张白底板
# 创建Font对象:
font = ImageFont.truetype('/usr/share/fonts/wps-office/FZXKK.TTF', 40)
#font =  ImageFont.load_default().font
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
#for t in range(4):
draw.text((60, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()
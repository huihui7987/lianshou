from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/usr/share/fonts/wps-office/FZXKK.TTF',size=300)
    fillcolor= '#ff0000'
    width,height = img.size
    draw.text((width-400,0),'99',font=myfont,fill = fillcolor)
    img.save('/home/huihui7987/文档/sq/python基础+高级/res.jpg','jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open('/home/huihui7987/文档/sq/python基础+高级/IMG_0353.jpg')
    add_num(image)
    image.show()

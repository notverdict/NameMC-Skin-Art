from PIL import Image
import os

def run(input):
    defaultamount = 28
    try:
        im = Image.open(input)
        imgwidth, imgheight = im.size
        height = imgheight // 3
        width = imgwidth // 9
        for i in range(0, 3):
            for j in range(0, 9):
                box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
                a = im.crop(box)
                defaultamount = defaultamount - 1
                img = a
                background = Image.open("head.png")
                background.paste(img, (8, 8), img)
                background.save(f'{str(defaultamount)}.png', "PNG")
        print('[!] Done.')
        os.system('pause >> NUL')
    except:
        print('[-] File not Found.')
        os.system('pause >> NUL')

png = input('[!] Image File Name: ')
run(png)
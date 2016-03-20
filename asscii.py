#!/usr/bin/env python
# coding=utf-8
#将图片转变为字符输出

from PIL import Image
import argparse

parse =argparse.ArgumentParser()
parse.add_argument('file')
parse.add_argument('-o','--output')
parse.add_argument('--width',type=int,default=40)
parse.add_argument('--height',type=int,default=40)

args= parse.parse_args()


IMG =args.file
WIDTH=args.width
HEIGHT = args.height
OUTPUT =args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.")

def get_char(r,b,g,alpha=256):
    if alpha ==0:
        return ' '
    length = len(ascii_char)
    #灰度值公式
    gray = int(0.2126*r+0.7152*g + 0.0722*b)

    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    im=Image.open(IMG)
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt=""
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

from PIL import Image
import random
from bisect import bisect

# greyscale.. the following strings represent
# 7 tonal ranges, from lighter to darker.
# for a given pixel tonal level, choose a character
# at random from that range.
 
greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "tRiD3pTr4i*Q",
            "pRoX",
            "#%$"
            ]
 
# using the bisect class to put luminosity values
# in various ranges.
# these are the luminosity cut-off points for each
# of the 7 tonal levels. At the moment, these are 7 bands
# of even width, but they could be changed to boost
# contrast or change gamma, for example.
 
zonebounds=[10,5,108,50,180,216,100]
 
# open image and resize
# experiment with aspect ratios according to font
 
im=Image.open(r"d:\test.jpg")
im=im.resize((160, 100),Image.BILINEAR)
im=im.convert("L") 
 
# now, work our way over the pixels
# build up str
 
str=""
for y in range(0,im.size[1]):
    for x in range(0,im.size[0]):
        lum=255-im.getpixel((x,y))
        row=bisect(zonebounds,lum)
        possibles=greyscale[row]
        str=str+possibles[random.randint(0,len(possibles)-1)]
    str=str+"\n"
 
print(str)
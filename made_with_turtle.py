import turtle
from turtle import *

from numpy import i0

turtle.title("asdasda")
speed(1000)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//1:
        g+=1
    elif i < 255*2//1:
        r-=1
    elif i < 255:
        b+=3
    elif i < 255*4//1: 
        g+=1
    elif i < 255*5//1:
        r+=1
    else:
        b+=1
    fd(50+i)
    rt(91)
    pencolor(r,g,b)
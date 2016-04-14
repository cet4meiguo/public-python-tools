#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
排序算法练习
"""
import random
import time
from Tkinter import *
def createdata(num):
    """随机生成0-10万之间的数,包括两边"""
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,100))
        i+=1
    return a


def insertsort(array,cv=None):
    """
    直接插入排序
    range(1,3)->1,2
    [0,1,2,3].pop() ->[0,1,2]
    [0,1,2,3].pop(0) ->[1,2,3]
    [0,1].insert(10,2)->[0,1,2]
    [0,1].insert(1,2) ->[0,2,1]
    数组必须有引用,否则单纯[0,1].insert(1,2)为None.
    """
    for i in range(1,len(array)):
        j=0
        while j<i and array[i]>array[j]: #if array[i]<array[j],降序
            j=j+1
        array.insert(j,array[i])
        array.pop(i+1)

    return array

def drawrectangle(canvas,width,height,array,max):
    """
    绘制array
    """
    for i in range(0,len(array)):
        canvas.create_rectangle((i*(width/len(array))),height-array[i]*((height/max)),
                                (i+1)*((width/len(array))),height,
                                fill='lightblue',outline='black')
def clone(array):
    new=[]
    for i in array:
        new.append(i)
    return new
def draw_insertsort(array):
    for i in range(1,len(array)):
        j=0
        while j<i and array[i]>array[j]: #if array[i]<array[j],降序
            j=j+1
        array.insert(j,array[i])
        array.pop(i+1)
        cv.delete(ALL)
        drawrectangle(cv,width,height,array,max)
root = Tk()
width=600
height=400
num=100
cv=Canvas(root,bg='white',width=width,height=height)

array=createdata(num)
sorted_array=insertsort(clone(array))
max=sorted_array[-1]
print(array)
print(max)
drawrectangle(cv,width,height,array,max)
draw_insertsort(array)
cv.pack()
root.mainloop()

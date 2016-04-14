#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
可视化插入排序算法.
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

def step(array):
    j=0
    while j<b[0] and array[b[0]]>array[j]: #if array[i]<array[j],降序
        j=j+1
    array.insert(j,array[b[0]])
    array.pop(b[0]+1)
    b[0]=b[0]+1
def update():
    def draw(width,height,array,max):
        if(b[0]==num):
            return
        
        step(array)
        cv.delete(ALL)
        drawrectangle(cv,width,height,array,max)
        cv.after(100,update)
    draw(width,height,array,max)                                 
root = Tk()
width=600
height=400
num=200
cv=Canvas(root,bg='white',width=width,height=height)

array=createdata(num)
sorted_array=sorted(array)
max=sorted_array[-1]
b=[1]
drawrectangle(cv,width,height,array,max)

#draw(width,height,array,max)
update()
cv.pack()
root.mainloop()

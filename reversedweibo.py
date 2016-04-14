#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
对监听保存的微博按正常顺序排序
"""
f=open('e:/invest.txt')
lines = f.readlines()
f.close()
s=''
options=[]
for line in lines:
    if line.startswith('rickwang02'):
        new = ''
        for option in options:
            new = new +option
        s = new + s
        options=[]
    else:
        options.append(line)

nf = open('e:/newinvest.txt','w')
nf.write(s)
nf.close()

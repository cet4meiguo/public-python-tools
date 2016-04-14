#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""对监听保存的微博按正常顺序排序"""
f=open('e:/invest.txt')
lines = f.readlines()
f.close()
options=[]
option=[]
for line in lines:
    if line.startswith('rickwang02'):
        options.append(option)
        option=[]
    else:
        option.append(line)

nf = open('e:/newwinvest.txt','a')
for line in reversed(options):
    for l in line:
        nf.write(l)
nf.close()

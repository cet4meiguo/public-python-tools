#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,os.path

"""
文件内容按行倒序排列.如果newWork已存在,会覆盖.
调用方式如:
reserve('e:/','work.txt','newWork.txt')
"""

def reserve(path,name,newName):
    file = open(path+name,'r')
    newpath = path+newName
    newFile = open(newpath,'w')
    lines = []  
    for line in file.readlines():
        lines.append(line)

    length = len(lines)
    while(length>0):
        length=length-1
        newFile.write(lines[length])
    file.close()
    newFile.close()


#!usr/bin/env
#-*- coding:utf-8 -*-
import os
"""
替换原文件中的内容
"""
properties = open("e:/text.txt",'rb+')
lines = properties.readlines()
d=""
for line in lines:
    c = line.replace("world", "world is modifiled")
    d += c
    properties.seek(0)      #不要让python记住执行到这里，从文件头还始
    properties.truncate()   #清空文件
    properties.write(d)
    properties.close()

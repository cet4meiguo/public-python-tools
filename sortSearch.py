#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
XX项目,高级查询配置文件各search按名称排序
"""
import re
path='f:/XX/source/search.xml'

file=open(path,'r')
newFile=open(path[0:-4]+'New.xml','a')
lines= file.readlines()
file.close()
search_items_start=False
search_items_end=False
column_items_start=False
column_items_end=False
block=[]
for line in lines:
    if re.search(r'<search-items>',line):
        search_items_start=True
        newFile.write(line)
        continue
    if re.search(r'</search-items>',line):
        search_items_end=True
    if search_items_start:
        if not search_items_end:
            block.append(line)
            continue
        else:
            block.sort()
            for a in block:
                newFile.write(a)
            block=[]
            newFile.write(line)
            search_items_start=False
            search_items_end=False
            continue
    else:
        newFile.write(line)
        continue
"""
    if re.search(r'<column-items>',line):
        search_items_start=True
        newFile.write(line)
        continue
    if re.search(r'</column-items>',line):
        search_items_end=True
        newFile.write(line)
        continue
    if search_items_start:
        if not search_items_end:
            block.append(line)
        else:
            block.sort()
            for a in block:
                newFile.write(a)
            block=[]
            newFile.write(line)
            search_items_start=False
            search_items_end=False
    else:
        newFile.write(line)
"""
newFile.close()


    
    

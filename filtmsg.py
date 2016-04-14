#!usr/bin/env python 2.7
#-*- coding:utf-8 -*-

import re
"""
过滤QQ聊天记录,只保留顿悟的发言.
"""
def filtmsg(path='e:/work/f.txt',qq='1800403'):
    file = open(path,'r')
    newfile = open('e:/work/fnew.txt','a')
    lines = file.readlines()
    start = False
    end = False
    for line in lines:
        if re.search(qq,line):
            print(line)
            start = True
        elif re.search(r'\d{4}-\d{2}-\d{2}\s+\d{1,2}:\d{1,2}:\d{1,2}\s+.*?\(\d{5,10}\)'
    ,line):
            end = True;

        if start and not end:
            newfile.write(line)
    file.close()
    newfile.close()

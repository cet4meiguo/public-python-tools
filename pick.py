#!usr/bin/env python
#-*- coding:utf-8 -*-
import re
def pick():
    file = open('e:/a.txt')
    text = file.readlines()
    for line in text:
        path = line.replace("\t","").replace("\n","")
        sourceFile = open('e:/b.txt')
        

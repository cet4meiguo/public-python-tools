#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
学习pattern.sub(func,s)用法.
"""
import re
p=re.compile(r'/wiki/(\w*)/?(\w*)')
s='/wiki/a;sdfs/wiki/b/c'



def func(m):
    print(m.groups())
    if(m.group(2)!=''):
        return m.group(1)+'.'+m.group(2)+'.html'
    else:
        return m.group(1)+'.html'

ss=p.sub(func,s)
print(ss)

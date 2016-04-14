#!/user/bin/env python
#-*- coding:utf-8 -*-
"""
在path目录下后缀为'.ext'的文件中查找内容 regex,regex为raw string.


"""
import os,re
def find(path,ext,regex):
    for root,dirs,files in os.walk(path):
        find_file(root,dirs,files,ext,regex)
def find_file(root,dirs,files,ext,regex):
    for file in files:
        
        path = os.path.join(root,file)
        path = os.path.normcase(path)
        try:
            fileType = os.path.splitext(file)[1]
        except:
            fileType = ''
        if ext!=fileType:
            continue;
        
        f = open(path,'r')
        try:
            for l in f.readlines():
                print(l)
                if re.search(regex,l):
                    print(path)
                    print(l)
                    break
        except UnicodeDecodeError:
            print('UnicodeDecodeError:%s' % path)


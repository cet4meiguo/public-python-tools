#!/usr/bin/env python
#-*- coding:utf-8-*-
import re
import os
"""
for each line in py files under 'e:/dropbox/python',
search regex
if match, return the whole path.
"""

def doFind(root,dirs,files,regex):
    """
    查找files文件内的内容,是否符合正则表达式
    """
    for file in files:
        if os.path.splitext(file)[1][1:]=='py': #splitext 得到的后缀为 .py
            path = os.path.join(root,file)
            path = os.path.normcase(path)
            #print('path:    %s' % path)
            f=open(path,'r')
            try:
                for l in f.readlines():
                    if re.search(regex,l):
                        print(path)
                        break
            except UnicodeDecodeError:
                print("UnicodeDecodeError,path:    %s" % path)
                f.close()
            f.close()
def find(root,regex):
    """
    在root目录下所有(子)文件/文件夹,
    查找包含content的文件,
    打印出文件路径
    """
    for context,dirs,files in os.walk(root):
        doFind(context,dirs,files,regex)
"""
root = "e:\\python"
content ="stat"
findContent(root,content)
"""
        

                

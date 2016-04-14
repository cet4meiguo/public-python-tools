#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,os.path
import re
import shutil
"""
查找jsp/html/htm页面 中是否有禁用缓存语句,缺少则添加.
"""
def modify_file(root,dirs,files):
    for file in files:
        path = os.path.join(root,file)
        if re.search(r".*\.jsp$",path) or re.search(r".*\.html$",path) or re.search(r".*\.htm$",path):
            modifyFile(path)
        else:
            newpath = 'e'+path[1:]
            parentFolder = os.path.split(newpath)
            try:
                os.makedirs(parentFolder[0])
            except (WindowsError):
                pass
            shutil.copy(path,'e'+path[1:])
pragma = '<meta http-equiv="pragma" content="no-cache">\n';
cache_control='<meta http-equiv="cache-control" content="no-cache">\n'
expires='<meta http-equiv="expires" content="0">\n'

def modifyFile(path):
    file = open(path,'r')
    newpath = 'e'+path[1:]
    parentFolder = os.path.split(newpath)
    try:
        os.makedirs(parentFolder[0])
    except (WindowsError):
        pass
    newFile = open(newpath,'a')
    headStart = False
    headEnd = False

    boolpragma=False;
    boolcache_control=False;
    boolexpires=False;
   
    for line in file.readlines():
        
        #查找
        if re.search(r'<head>',line):
            headStart = True;
           
        if headStart and not headEnd:
            if re.search(r'http-equiv="pragma"',line):
                boolpragma = True
            if re.search(r'http-equiv="cache-control"',line):
                boolcache_control = True
            if re.search(r'http-equiv="expires"',line):
                boolexpires = True
            if re.search(r'</head>',line):
                headEnd = True
                if not boolpragma:
                   newFile.write(pragma)
                   print(newpath)
                if not boolcache_control:
                   newFile.write(cache_control)
                   print(newpath)
                if not boolexpires:
                   newFile.write(expires)
                   print(newpath)
                newFile.write(line)
            else:
                newFile.write(line)
        else:
           newFile.write(line)
    file.close()
    newFile.close()
    print('----------------------------------')
def modifyAll():
    for root,dirs,files in os.walk("f:/nocache"):
        modify_file(root,dirs,files)

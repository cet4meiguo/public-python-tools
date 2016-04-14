#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,os.path
import re
def rename(file):
    files = os.path.splitext(file)
    file = files[0]+str(0)+files[1]
    if os.path.isfile(file):
        return rename(file)
    return file
def copyImage(root,dirs,files):
    for file in files:
            path = os.path.join(root,file)
            path = os.path.normcase(path)
            new = 'e:\\secret\\phone2\\'+path[3:]
            if re.search(r".*\.png$",path) or re.search(r".*\.gif$",path)\
               or re.search(r".*\.jpg",path) or re.search(r".*\.jpeg",path):
                if os.path.isfile(new):
                    new = rename(new)
                print (path)
                print(new)
                parentFolder = os.path.split(new)
                try:
                    os.makedirs(parentFolder[0])
                except (WindowsError):
                    pass
                shutil.copy(path,new)
for root,dirs,files in os.walk("h:/"):
    copyImage(root,dirs,files)

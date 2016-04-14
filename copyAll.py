#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,os.path
import re
import shutil

"""
将文件夹下所有文件逐个拷贝到另一目录下.
不整体拷贝是因为目的目录可能还有其他文件,此法可保证不破坏目标文件夹.
"""
ROOT='f:/mobile/'
TOROOT='E:/XXX/'
def copy_file(root,dirs,files,ROOT,TOROOT):
    for file in files:
        path = os.path.join(root,file)
        print(path)
        newFile = TOROOT+path[len(ROOT):]
        print(newFile)
        parentFolder = os.path.split(newFile)
        try:
            os.makedirs(parentFolder[0])
            print('os.makedirs:\t%s' % parentFolder[0])
        except (WindowsError):
            pass
        shutil.copy(path,newFile)
        print('-------------')
        
def copyAll(ROOT=ROOT,TOROOT=TOROOT):
    for root,dirs,files in os.walk(ROOT):
        copy_file(root,dirs,files,ROOT,TOROOT)
copyAll()

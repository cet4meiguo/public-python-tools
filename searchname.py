#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,os.path
import re
def print_pdf(root,dirs,files,fileType,contains):
    for file in files:
            path = os.path.join(root,file)
            path = os.path.normcase(path)
            if re.search(r".*"+contains+".*\."+str(fileType)+"$",path):
                print(path)
def search(path,fileType,contains):
    for root,dirs,files in os.walk(path):
        print_pdf(root,dirs,files,fileType,contains)    

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import time
import re
"""
        1.copy change log files from svn,
        2.save as rootPath/now(such as:13.06.15)/change.txt
        3.run gather()
        4.ftp now folder to ftp(c:/deploy/ftp/)
        5.run deploy()
"""
pathFile='e:/libs.txt'
toPath="e:/libs/"

def gather():
    file = open(pathFile)
    text = file.readlines()
    for line in text:
        line=line.replace('\n','')
        p=os.path.split(line)
        filePath = p[1]
        parentFolder = os.path.split(toPath+filePath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        shutil.copy(line, toPath+filePath)
gather()

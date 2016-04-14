#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import time
import re
import ConfigParser
"""
        1.copy change log files from svn,
        2.save as rootPath/now(such as:13.06.15)/change.txt
        3.run gather()
        4.ftp now folder to ftp(c:/deploy/ftp/)
        5.run deploy()
"""
def deploy():
    """
        waitex rootPath :"c:/deploy/ftp/"
        test rootPath:"f:/XX/source/"
    """
    rootPath = 'c:/deploy/ftp/'
    toRootPath = 'c:/deploy/XX'
    pathFile = 'change.txt'
    project = 'XX'
	
    now = time.strftime('%y.%m.%d',time.localtime(time.time()))
    fromPath = rootPath + now
    pathFile = rootPath + now +"/" + pathFile
    file = open(pathFile)
    text = file.readlines()
    for line in text:
        filePath = line.replace("\t","").replace("\n","").replace("java","class")

        if re.search(project+"Web/src",filePath):
            filePath = filePath.replace(project+"Web/src",project+"web/web-inf/classes")
        elif re.search(project+"Web/WebRoot",filePath):
            filePath = filePath.replace(project+"Web/WebRoot",project+"web")
        elif re.search(project+"EJB/src",filePath):
            filePath = filePath.replace(project+"EJB/src",project+"ejb")
        print("From path: %s " % fromPath)
        print("File path: %s " % filePath)
        print("From path:%s " % fromPath+filePath)
        print("**To path:%s" % toRootPath+filePath)
        parentFolder = os.path.split(toRootPath+filePath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        
        shutil.copy(fromPath+filePath,toRootPath+filePath)
deploy()
raw_input('Press any key to exit.')

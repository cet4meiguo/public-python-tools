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
def gather():
    """
        fromRootPath only specify the root path,which paths in pathFile need.
    """
    config = ConfigParser.ConfigParser()
    with open('config.ini') as cfgfile:
        config.readfp(cfgfile)
        rootPath = config.get('info','rootPath')
        fromRootPath = config.get('info','fromRootPath')
        pathFile = config.get('info','pathFile')
        project = config.get('info','project')

    now = time.strftime('%y.%m.%d',time.localtime(time.time()))
    toPath = rootPath+now
    print("To path: %s" % toPath)
    pathFile = rootPath +now+"/"+pathFile
    print("Path file: %s" % pathFile)
    
    file = open(pathFile)
    text = file.readlines()
    for line in text:
        filePath = line.replace("\t","").replace("\n","").replace("java","class")
        print("From file: %s " % filePath)

        if re.search(project+"Web/src",filePath):
            filePath = filePath.replace(project+"Web/src",project+"web/web-inf/classes")
        elif re.search(project+"Web/WebRoot",filePath):
            filePath = filePath.replace(project+"Web/WebRoot",project+"web")
        elif re.search(project+"EJB/src",filePath):
            filePath = filePath.replace(project+"EJB/src",project+"ejb")
        print("From file: %s " % filePath)            
        """
            without Hierarchy forder
            shutil.copy(fromRootPath + filePath, toPath)
        """
        print(toPath+filePath)
        parentFolder = os.path.split(toPath+filePath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        shutil.copy(fromRootPath + filePath, toPath+filePath)
gather()
raw_input('Press any key to exit.')
        
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import time
import re
import ConfigParser
import traceback
"""
        1.copy change log files from svn,
        2.save as rootPath/now(such as:13.06.15)/change.txt
        3.run gather()
        4.ftp now folder to ftp(c:/deploy/ftp/)
        5.run deploy()

        6.update
        保留SVN log中 操作编号(M,A,D)
        
"""
def gather():
    """
        fromRootPath only specify the root path,which paths in pathFile need.
    """
    #"""
    rootPath = 'f:/XX/source/'
    fromRootPath = 'D:/Oracle/Middleware/user_projects/domains/XX/autodeploy/XX3PL'
    pathFile = 'change.txt'
    project = 'XX3PL'
    """
    config = ConfigParser.ConfigParser()
    with open('config.ini') as cfgfile:
        config.readfp(cfgfile)
        rootPath = config.get('info','rootPath')
        fromRootPath = config.get('info','fromRootPath')
        pathFile = config.get('info','pathFile')
        project = config.get('info','project')
    """

    now = time.strftime('%y.%m.%d',time.localtime(time.time()))
    toPath = rootPath+now
    print("To path: %s" % toPath)
    pathFile = rootPath +now+"/"+pathFile
    print("Path file: %s" % pathFile)
    
    file = open(pathFile)
    text = file.readlines()
    fileCounts = 0
    exceptionCount = 0
    for line in text:
        filePath = line.replace(" ","").replace("\t","").replace("\n","").replace("java","class")
        print("SVN Log:\n%s" % filePath)

        operate = filePath[0]
        filePath = filePath[1:]
        
        if re.search(project+"Web/src",filePath):
            filePath = filePath.replace(project+"Web/src",project+"web/web-inf/classes")
        elif re.search(project+"Web/WebRoot",filePath):
            filePath = filePath.replace(project+"Web/WebRoot",project+"web")
        elif re.search(project+"EJB/src",filePath):
            filePath = filePath.replace(project+"EJB/src",project+"ejb")
        elif re.search(project+"/",filePath):
            filePath = filePath.replace(project+"/",'')
        print("From file:\n%s%s" % (fromRootPath,filePath))
        """
            without Hierarchy forder
            shutil.copy(fromRootPath + filePath, toPath)
        """
        print("To file:\n%s%s\n" % (toPath,filePath))
        parentFolder = os.path.split(toPath+filePath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        
        if operate =='M' or operate =='A':
            try:
                shutil.copy(fromRootPath + filePath, toPath+filePath)
            except(IOError):
                exceptionCount+=1
                traceback.print_exc()
        else:
            pass
        fileCounts+=1

    print('Total files:\t\t%d\nException files:\t%d' % (fileCounts,exceptionCount))
try:
    gather()
except:
    traceback.print_exc()
raw_input('Press enter key to exit.')
    

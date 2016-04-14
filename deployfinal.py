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

        6:update
        保留SVN log中 操作编号(M,A,D)
"""
def deploy():
    """
        XX rootPath :"c:/deploy/ftp/"
        test rootPath:"f:/XX/source/"
    """
    """
    rootPath = 'c:/deploy/ftp/'
    toRootPath = 'c:/deploy/XX'
    pathFile = 'change.txt'
    project = 'XX'
    """
    config = ConfigParser.ConfigParser()
    with open('config.ini') as cfgfile:
        config.readfp(cfgfile)
        rootPath = config.get('info','rootPath')
        toRootPath = config.get('info','toRootPath')
        pathFile = config.get('info','pathFile')
        project = config.get('info','project')
    
    now = time.strftime('%y.%m.%d',time.localtime(time.time()))
    fromPath = rootPath + now
    pathFile = rootPath + now +"/" + pathFile
    file = open(pathFile)
    text = file.readlines()
    fileCounts = 0
    exceptionCounts = 0
    for line in text:
        filePath = line.replace(" ","").replace("\t","").replace("\n","").replace("java","class")
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
        print("From path: %s " % fromPath)
        print("File path: %s " % filePath)
        print("From path:%s " % fromPath+filePath)
        print("**To path:%s" % toRootPath+filePath)
        parentFolder = os.path.split(toRootPath+filePath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        if operate =='M' or operate =='A':
            try:
                shutil.copy(fromPath+filePath,toRootPath+filePath)
            except(IOError):
                traceback.print_exc()
                exceptionCounts+=1
        else:
            try:
                if os.path.isdir(toRootPath+filePath):
                    shutil.rmtree(toRootPath+filePath)
                else:
                    os.remove(toRootPath+filePath)
            except(WindowsError):
                traceback.print_exc()
                exceptionCounts+=1
            except(IOError):
                traceback.print_exc()
                exceptionCounts+=1
        fileCounts +=1
    print('Total files:\t\t%d\nException files:\t%d' % (fileCounts,exceptionCounts))
try:
    deploy()
except:
    traceback.print_exc()
raw_input('Press any key to exit.')

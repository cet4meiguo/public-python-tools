#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
读取filteredchange.txt文件
读取原代码
读取编译后的文件
如果找不到文件,则为删除,pass
"""
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

        6.update
        保留SVN log中 操作编号(M,A,D)
        
"""
def control():
    """
        fromRootPath only specify the root path,which paths in pathFile need.
    """
    """
    config = ConfigParser.ConfigParser()
    with open('config.ini') as cfgfile:
        config.readfp(cfgfile)
        rootPath = config.get('info','rootPath')
        fromRootPath = config.get('info','fromRootPath')
        pathFile = config.get('info','pathFile')
        project = config.get('info','project')
    """
    rootPath = 'f:/waitex/version/'
    fromRootPath = 'D:/Oracle/Middleware/user_projects/domains/waitex/autodeploy/Waitex3PL'
    fromRootPathForSource = 'E:/Dropbox/yicomm/Waitex3PL/code'
    pathFile ='filteredchange.txt'
    project = 'Waitex3PL'
    
    now = time.strftime('%y.%m.%d',time.localtime(time.time()))
    toPath = rootPath+now+'/class'
    toPathForSource = rootPath+now+'/source'
    print("To path: %s" % toPath)
    pathFile = rootPath +now+"/"+pathFile
    print("Path file: %s" % pathFile)
    
    file = open(pathFile)
    text = file.readlines()
    fileCounts = 0
    for line in text:
        gatherSource(rootPath,fromRootPathForSource,toPathForSource,project,line)
        gatherClass(rootPath,fromRootPath,toPath,project,line)
        

    print('Total files: %d' % fileCounts)
def gatherClass(rootPath,fromRootPath,toPath,project,line):
    filePath = line.replace(" ","").replace("\t","").replace("\n","").replace("java","class")
    print("SVN Log: %s" % filePath)
    
    #operate = filePath[0]
    #filePath = filePath[1:]
    
    if re.search(project+"Web/src",filePath):
        filePath = filePath.replace(project+"Web/src",project+"web/web-inf/classes")
    elif re.search(project+"Web/WebRoot",filePath):
        filePath = filePath.replace(project+"Web/WebRoot",project+"web")
    elif re.search(project+"EJB/src",filePath):
        filePath = filePath.replace(project+"EJB/src",project+"ejb")
    print("From file: %s " % filePath)            
    """
        without Hierarchy forder
        shutil.copy(0fromRootPath + filePath, toPath)
    """
    newPath = toPath+filePath
    if os.path.isfile(fromRootPath+filePath):
        parentFolder = os.path.split(newPath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        shutil.copy(fromRootPath + filePath, newPath)
    else:
        print('Delete: %s' % newPath)
def gatherSource(rootPath,fromRootPathForSource,toPath,project,line):
    filePath = line.replace(" ","").replace("\t","").replace("\n","")
    print("SVN Log: %s" % filePath)
    
    #operate = filePath[0]
    #filePath = filePath[1:]        
    newPath = toPath+filePath
    if os.path.isfile(fromRootPathForSource + filePath):
        parentFolder = os.path.split(newPath)
        try:
            os.makedirs(parentFolder[0])
        except (WindowsError):
            pass
        
        shutil.copy(fromRootPathForSource + filePath, newPath)
    else:
        print('Delete: %s' % newPath)
control()
raw_input('Press any key to exit.')

    

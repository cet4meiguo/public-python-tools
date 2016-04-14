#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
批量修改文件
"""
import os,os.path
import re
import shutil

def modify_file(root,dirs,files):
    for file in files:
        path = os.path.join(root,file)
        
        if re.search(r".*\.jsp$",path):
            modifyFile(path)
        """
        else:
            newpath = 'e'+path[1:]
            parentFolder = os.path.split(newpath)
            try:
                os.makedirs(parentFolder[0])
            except (WindowsError):
                pass
            shutil.copy(path,'e'+path[1:])
"""

def modifyFile(path):
    file = open(path,'r')
    newpath = 'e'+path[1:]
    parentFolder = os.path.split(newpath)
    try:
        os.makedirs(parentFolder[0])
    except (WindowsError):
        pass
    newFile = open(newpath,'a')
    imgStart = False
    actionStart = False
    actionEnd = False
    imgList = []
    actionList = []
    menuName =''
    imgNew = "src='<s:property value='#udf.toolbarimgpath'/>"
    imgNew2 = "src=\"<s:property value='#udf.toolbarimgpath'/>"
    
    for line in file.readlines():
        #查找
        if re.search(r'image/toolbar',line):
            imgStart = True
            line = re.sub(r'src=".*.gif',imgNew2,line)
            line = re.sub(r"src='.*.gif",imgNew,line)
        if re.search(r'<s:action',line):
            actionStart = True;
            imgStart = False
        if re.search(r'</s:action',line):
            actionEnd = True;
            #menuName紧跟后面
            if re.search(r'<s:property',line):
                po = line.index('<s:property')
                left = line[0:po]
                menuName = line[po:]
                line = left+'\n'
        if imgStart and not actionStart:
            imgList.append(line)
        if actionStart:
            actionList.append(line)

        #imgStart 与 actionStart同时发生
        if imgStart and actionStart:
            print('__________E R R O R __________')
        #actionStart 与actionEnd同时发生
        if actionStart and actionEnd:
            pass
        if actionEnd:
        #先写actionList,再写imgList
            for action in actionList:
                newFile.write(action)
            for img in imgList:
                newFile.write(img)
            if len(menuName)>0:
                newFile.write(menuName)
            imgStart = False
            actionStart = False
            actionEnd = False
            continue
            
        if not actionEnd and not imgStart and not actionStart:
            newFile.write(line)
    file.close()
    newFile.close()
def modifyAll():
    for root,dirs,files in os.walk("f:/mobile"):
        modify_file(root,dirs,files)

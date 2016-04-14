#-*- coding:utf-8 -*-
"""
IOS plist 省市区文件 转化为Android普通XML 文件
"""
import Tkinter as tk
import re
import urllib2
import socket
import time
import threading
import winsound

def reserve(path,name,newName):
    file = open(path+name,'r')
    newpath = path+newName
    newFile = open(newpath,'w')
    lines = []
    p_value=r'<string>(.*)</string>'
    header="""<root>"""
    end="""\n</root>"""
    newFile.write(header)
    dictStart=keyStart=False
    cities=[]
    for line in file.readlines():
        if re.findall('<dict>',line):
            dictStart=True
        if re.findall('<key>state</key>',line):
            keyStart=True
        p= re.findall(p_value,line)
        if p and dictStart:
            if not keyStart:
                cities.append(p[0])
            else:
                newFile.write('\n\t<province name="%s">' % p[0])
                for i in cities:
                    newFile.write('\n\t\t<city name="%s"></city>'%i)
                newFile.write('\n\t</province>')
                dictStart=False
                keyStart=False
                cities=[]
    newFile.write(end)
    file.close()
    newFile.close()
    
reserve('d:/','area1.plist','province_data_long.xml')

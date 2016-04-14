#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
省市区js文件转化为 province_data.xml文件
"""
import Tkinter as tk
import re
import urllib2
import socket
import time
import threading
import winsound
import json
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
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
    j=json.load(file)
    print(type(j))
    print(type(j[0]))
    for jj in j:
        newFile.write('\n\t<province name="%s">' % (jj['value']))
        states = jj['states']
        for state in states:
            newFile.write('\n\t\t<city name="%s">' % (state['value']))
            dicts = state['cities']
            for d in dicts:
                newFile.write('\n\t\t\t<district name="%s"/>' % (d['value']))
            newFile.write('\n\t\t</city>')
        newFile.write('\n\t</province>')
    newFile.write(end)
    file.close()
    newFile.close()
"""
    for jj in j:
        newFile.write('\n\t<province name="%s" code="%s">' % (jj['value'],jj['code']))
        states = jj['states']
        for state in states:
            newFile.write('\n\t\t<city name="%s" code="%s">' % (state['value'],state['code']))
            dicts = state['cities']
            for d in dicts:
                newFile.write('\n\t\t\t<district name="%s" code="%s" />' % (d['value'],d['code']))
            newFile.write('\n\t\t</city>')
        newFile.write('\n\t</province>')
    newFile.write(end)
    file.close()
    newFile.close()
"""

reserve('e:/','cd.js','province_data.xml')
file = open('e:/cd.js')
j=json.load(file)
print(type(j[0]['states']))
ss=j[0]['states']
for s in ss:
    print(type(s))
bj=ss[0]
print(type(bj))






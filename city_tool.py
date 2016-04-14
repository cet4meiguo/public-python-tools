#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
xml 转plist
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

    #
    p_provience=r'province name="(.*?)"'
    p_city=r'city name="(.*?)"'
    p_district=r'district name="(.*?)"'
    #pp_p=re.compile(p_provience)
    header="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
"""
    end="""</array>\n</plist>"""
    state_header="""	<dict>
		<key>cities</key>
		<array>\n"""
    state_end="""\t\t</array>
		<key>state</key>
		<string>"""
    state_end_true=state_end+"%s</string>\n\t</dict>\n"


    district_header="""	        <dict>
                <key>districts</key>
                <array>\n"""
    district_end="""\t\t\t\t</array>
                <key>city</key>
                    <string>"""
    district_end_true=district_end+"%s</string>\n\t\t\t</dict>\n"
    
    newFile.write(header)
    
    #核心
    pr=''
    cr=''
    """
    for line in file.readlines():
        province=re.findall(p_provience,line)
        if province :
            pr=province[0]
            newFile.write(state_header)
            print(province[0])
        city=re.findall(p_city,line)
        if city and len(city)>0:
            newFile.write("\t\t\t<string>%s</string>\n" % city[0])
        city_end = re.findall(r'</province>',line)
        if city_end:
            newFile.write(state_end_true % pr)
    """
    for line in file.readlines():
        province=re.findall(p_provience,line)
        if province :
            pr=province[0]
            newFile.write(state_header)
            print(province[0])
            
        city=re.findall(p_city,line)
        if city:
            cr=city[0]
            newFile.write(district_header)
            print(city[0])
        city_end = re.findall(r'</province>',line)
        if city_end:
            newFile.write(state_end_true % pr)
        district = re.findall(p_district,line)
        if district and len(district)>0:
            newFile.write("\t\t\t\t\t<string>%s</string>\n" % district[0])
        district_end = re.findall(r'</city>',line)
        if district_end:
            newFile.write(district_end_true % cr)

            
    newFile.write(end)
    file.close()
    newFile.close()

reserve('e:/','province_data.xml','new_province_data.xml')

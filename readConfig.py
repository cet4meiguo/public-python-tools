#!usr/bin/env python
#-*- coding:utf-8 -*-
import os
import ConfigParser

def readConfig():
    config = ConfigParser.ConfigParser()
    with open('config.ini') as cfgfile:
        config.readfp(cfgfile)
        config.set('info','age','22')
        name = config.get('info','name')
        age = config.get('info','age')
        print name
        print age

        config.set('info','gender','male')
        gender = config.get('info','gender')
        print gender
        
        
        
    

#!/user/bin/env python
#-*- coding:utf-8 -*-

import os,re
from stat import *
def find(where='.*',content=None,start='.',ext=None,logic=None):
    context={}
    context['where']=where
    context['content']=content
    context['return']=[]

    for root,dirs,files in os.walk(start):
        find_file(context,root,files)

    return context['return']
def find_file(context,dir,files):
    for file in files:
        path = os.path.join(dir,file)
        path = os.path.normcase(path)
        try:
            ext = os.path.splitext(file)[1][1:]
        except:
            ext = ''
        stat =os.stat(path)
        size = stat[ST_SIZE]

        # Do filtration based on the original parameters of find()
        if not re.search(context['where'],file):continue
        
        if context['content']:
            f = open(path,'r')
            match = 0
            try:
                for l in f.readlines():
                    if re.search(context['content'],l):
                        match = 1
                        break
            except UnicodeDecodeError:
                print('UnicodeDecodeError:%s' % path)
            if not match:continue

        file_return = (path,file,ext,size)
        context['return'].append(file_return)

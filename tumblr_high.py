#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
爬虫：爬tumblr

python 正则表达式参考:http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

"""
import urllib2
import urllib
import re
import os 
import threading
import time
import socket
nick='ddtskullbreaker'      #tumblr账户昵称
rootPath='D:/%s/' % nick    #本地保存文件夹.
jobs=20
page=0
timeout =20
sleep_time=10
def gethtml(url):
    """
    获取网页内容,并保存到本地.返回内容.
    """
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.98 Safari/537.23'}
        socket.setdefaulttimeout(timeout)
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        return html
    except urllib2.HTTPError, exc:
        if exc.code == 404:
            print "Not found !"
        else:          
            print "HTTP request failed with error %d (%s)" % (exc.code, exc.msg)
    except urllib2.URLError, exc:
        print "Failed because:", exc.reason
    except socket.timeout,e:
        try:
            time.sleep(sleep_time)
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
            return html
        except socket.timeout,e:
            pass
def getImage(permalink):
    name=os.path.split(permalink)[1]
    resourcepath = rootPath+name
    print("%s" % permalink)
    try:
        urllib.urlretrieve(permalink,resourcepath)
    except IOError:
        print("Retry: %s" % permalink)
        urllib.urlretrieve(permalink,resourcepath)
def getFromShort(shortUrl):
    code=gethtml(shortUrl)
    permalinks=re.findall(r'[src|href|content]="(http://[\w|.]+.tumblr.com/[\w|/]+.[gif]+)"',code) #[\s\S]*? 代替换行
    if len(permalinks)>0:
        for permalink in permalinks:
            name=os.path.split(permalink)[1]
            resourcepath = rootPath+name
            print("%s" % permalink)
            urllib.urlretrieve(permalink,resourcepath)
            
class Timer(threading.Thread):
    def __init__(self,num,interval,nick):
        threading.Thread.__init__(self)
        self.thread_num=num
        self.interval = interval
        self.thread_stop=False
    def stop(self):
        self.thread_stop = True
        
    def run(self):
        global page
        while not self.thread_stop:
            threadLock.acquire()
            page = page+1
            threadLock.release()
            code=gethtml('http://%s.tumblr.com/page/%d' % (nick,page))
            """
            #2015.3,28  修正
            p=r'[src|content]="(http://[\w|.]+.tumblr.com/[\w|/]+.[png|jpg|jpeg]+)"'
            
            """
            p_photoset=r'src="(http://[\w|.]+.tumblr.com/post/\d+/photoset_iframe/[\w|/]+/false)'
            m_photoset=re.findall(p_photoset,code)
            p=r'[href]="(http://[\w|.]+.tumblr.com/[\w|/]+.[png|jpg|jpeg]+)"'#2015.3.28
            
            pgif=r'[src|href|content]="(http://%s.tumblr.com/post/\d+)"'% nick
            test1=r'data-post-id'
            m=re.findall(p,code)
            mgif=re.findall(pgif,code)
            mtest1=re.findall(test1,code)
            if len(mtest1)<1 and len(mgif)<1:
                print('Thread '+str(self.thread_num)+' stoped!')
                self.stop()
            if len(m_photoset)>=1:
                for mm in m_photoset:
                    mm_code=gethtml(mm)
                    mmm=re.findall(p,mm_code)
                    for pp in mmm:
                        getImage(pp)
            if len(m)<1:
                pass
            else:
                for permalink in m:
                    getImage(permalink)
                    """
                    name=os.path.split(permalink)[1]
                    resourcepath = rootPath+name
                    print("%s" % permalink)
                    try:
                        urllib.urlretrieve(permalink,resourcepath)
                    except IOError:
                        print("Retry: %s" % permalink)
                        urllib.urlretrieve(permalink,resourcepath)
                    """
            if len(mgif)<1:
                pass
            else:
                #"""
                for url in mgif:
                    getFromShort(url)
                #"""
            time.sleep(self.interval)   #@modified 2015.3.28
try:
    os.makedirs(rootPath)   #创建目录
except (WindowsError):
    pass
threads=[]
threadLock=threading.Lock()
for i in range(jobs):
    t=Timer(i,2,nick)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print('End')

#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
爬虫：爬tumblr

modify nick,and run.
python 正则表达式参考:http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

"""
import urllib2
import urllib
import re
import os 
import threading
import time
nick='girlover6969' #Modify this nick,and run.
rootPath='e:/%s/' % nick  #本地保存文件夹.
jobs=200
page=0
def gethtml(url):
    """
    获取网页内容,并保存到本地.返回内容.
    """
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22'}
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
        global page                 # for modify 
        while not self.thread_stop:
            threadLock.acquire()    # Lock page num.
            page = page+1
            threadLock.release()    #
            code=gethtml('http://%s.tumblr.com/page/%d' % (nick,page))
            p=r'[src|content]="(http://[\w|.]+.tumblr.com/[\w|/]+.[png|jpg|jpeg]+)"'
            
            pgif=r'[src|href|content]="(http://%s.tumblr.com/post/\d+)"'% nick
            test1=r'data-post-id'
            m=re.findall(p,code)
            mgif=re.findall(pgif,code)
            mtest1=re.findall(test1,code)
            if len(mtest1)<1 and len(mgif)<1:
                #print('Thread '+str(self.thread_num)+' stoped!')
                self.stop()
                a=[]
                for t in threads:
                    if t.thread_stop:
                        a.append(t.thread_num)
                print(a)
            if len(m)<1:
                pass
            else:
                for permalink in m:
                    name=os.path.split(permalink)[1]
                    resourcepath = rootPath+name
                    #print("%s" % permalink)
                    urllib.urlretrieve(permalink,resourcepath)
            if len(mgif)<1:
                pass
            else:
                for url in mgif:
                    getFromShort(url)
                
            #time.sleep(self.interval)
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

#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
爬虫：爬weibo 相册

modify nick,and run.
python 正则表达式参考:http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

"""
import urllib2
import urllib
import re
import os 
import threading
import time
nick='3968797306' #Modify this nick,and run.
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
            code=gethtml('http://photo.weibo.com/%s/talbum/index#!/mode/1/page/%d' % (nick,page))
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
def run():
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
#run()
#encoding=utf-8
import urllib2
import urllib
import cookielib
def renrenBrower(url,user,password):
    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
    login_page = "http://www.renren.com/PLogin.do"
    try:
        #获得一个cookieJar实例
        cj = cookielib.CookieJar()
        #cookieJar作为参数，获得一个opener的实例
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        #生成Post数据，含有登陆用户名密码。
        data = urllib.urlencode({"email":user,"password":password})
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        opener.open(login_page,data)
        #以带cookie的方式访问页面
        op=opener.open(url)
        #读取页面源码
        data= op.read()
        return data
    except Exception,e:
        print str(e)
#访问某用户的个人主页，其实这已经实现了人人网的签到功能。
print renrenBrower("http://www.renren.com/home","用户名","密码")
code=gethtml('http://photo.weibo.com/%s/talbum/index#!/mode/1/page/%d' % (nick,page))
p=r'href="(http://photo.weibo.com/%s/talbum/detail/photo_id/\d+)"' % nick
m=re.findall(p,code)
print(p)
print(code)
for mm in m:
    print(mm)

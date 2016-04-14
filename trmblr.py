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
__all__=['gethtml','start','getcss','getjs','getimage']

starturl='http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000'
domain='http://www.liaoxuefeng.com/wiki/'
rootPath='e:/tumblr/'  #本地保存文件夹.

def gethtml(url):
    """
    获取网页内容,并保存到本地.返回内容.
    """
    print("URL:\t%s" % url)
    try:
        urlfile = urllib2.urlopen(url)
        source = urlfile.read()
        urlfile.close()
        #html = source.decode('utf-8')
        return source
    except urllib2.HTTPError, exc:
        if exc.code == 404:
            print "Not found !"
        else:          
            print "HTTP request failed with error %d (%s)" % (exc.code, exc.msg)
    except urllib2.URLError, exc:
        print "Failed because:", exc.reason
def createShortUrl(nick,num):
    """
    根据昵称与数字,组装shortUrl
    """
    return 'http://'+str(nick)+'tumblr.com/post/'+str(num)
def getFromShort(shortUrl):
    
    code=gethtml(shortUrl)
    permalinks=re.findall(r'permalink[\s\S]*?<img src="(.*?gif)',code) #[\s\S]*? 代替换行
    if len(permalinks)>0:
        for permalink in permalinks:
            name=os.path.split(permalink)[1]
            resourcepath = rootPath+name
            print("URL:\t%s" % permalink)
            urllib.urlretrieve(permalink,resourcepath)
def run():
    try:
        os.makedirs(rootPath)   #创建目录
    except (WindowsError):
        pass
    file=open('e:/chikcs  Archive.htm','r')
    content = file.read()
    links = re.findall(r'(http://chikcs.tumblr.com/post/\d*)"',content)
    if len(links)>0:
        for link in links:
            getFromShort(link)
    
test='http://test.tumblr.com/post/32621722193'
run()

def func(m):
    """
    /wiki/a/b
    替换为
    a.b.html
    或
    /wiki/a
    替换为
    a
    """
    if(m.group(2)!=''):
        s = m.group(1)+'.'+m.group(2)+'.html'
    else:
        s= m.group(1)+'.html'
    return s

def start():
    """
    抓取首页内容,查找地址列表,循环地址列表抓取内容.
    """
    try:
        os.makedirs(rootPath)   #创建目录
    except (WindowsError):
        pass
    source=gethtml(starturl)
    #css,js文件保存到本地.
    getcss()
    getjs()
    #获取匹配的url列表,为各章节地址.
    pattern=re.compile(r'/wiki/(\w*[/]?\w*)')
    urls=re.findall(pattern,source)
    #将url中 / 改为.准备工作
    filenamepattern=re.compile(r'(/)')
    #章节目录改为本地文件名
    menupattern=re.compile(r'/wiki/(\w*)/?(\w*)')
    #href="/themes/改为href="e:/git/themes/,e:/git/ 用rootPath
    cssjspattern=re.compile(r'href="/(themes/)')
    #<img src="/api" 替换为<img src="e:/git/api".
    imagepattern=re.compile(r'<img src="/(api/.*?)/url')
    getimage(source)
    for url in urls:
        source = gethtml(domain+url)
        getimage(source)
        #将url中 / 改为.
        name=filenamepattern.sub(r'.',url)

        #修改页面内章节目录连接.
        source=menupattern.sub(func,source)
        #修改css/js连接.
        source=cssjspattern.sub(r'href="%s\g<1>'% rootPath,source)
        #修改图片链接.
        source=imagepattern.sub(r'<img src="%s\g<1>.png' % rootPath,source)
        #保存本地
        file=open(rootPath+name+'.html','w')
        file.write(source)
        file.close()
def getcss():
    """
    css文件保存到本地.
    """
    source=gethtml(starturl)
    cssPattern = re.compile(r'(/themes.*?\.css)')
    csses=re.findall(cssPattern,source)
    for css in csses:
        csshref = cssPattern.sub(r'http://www.liaoxuefeng.com\g<1>',css)
        source = gethtml(csshref)
        if source:
            csspath = rootPath+css
            parentfolder = os.path.split(csspath)
            try:
                os.makedirs(parentfolder[0])
            except (WindowsError):
                pass
            file = open(csspath,'w')
            file.write(source)
            file.close()
def getjs():
    """
    js文件保存到本地.
    """
    source=gethtml(starturl)
    cssPattern = re.compile(r'(/themes.*?\.js)')
    csses=re.findall(cssPattern,source)
    for css in csses:
        csshref = cssPattern.sub(r'http://www.liaoxuefeng.com\g<1>',css)
        source = gethtml(csshref)
        if source:
            csspath = rootPath+css
            parentfolder = os.path.split(csspath)
            try:
                os.makedirs(parentfolder[0])
            except (WindowsError):
                pass
            file = open(csspath,'w')
            file.write(source)
            file.close()
def getimage(source):
    """
    图片下载 使用urllib.urlretrieve(url,path)
    源代码:src="/api/resources/001374713236987f0e694e1a02a4a538eaab311bb26a0bb000/url"
    实际请求      url: http://www.liaoxuefeng.com/api/resources/001374713236987f0e694e1a02a4a538eaab311bb26a0bb000/url
    保存本地位置 path: e:/git/api/resources/001374713236987f0e694e1a02a4a538eaab311bb26a0bb000.png
    """
    pattern = re.compile(r'(api/.*?)(?=/url)')
    resources=re.findall(pattern,source)
    for resource in resources:
        resourcehref = pattern.sub(r'http://www.liaoxuefeng.com/\g<1>',resource+'/url')
        
        resourcepath = rootPath+resource+".png"
        parentfolder = os.path.split(resourcepath)
        try:
            os.makedirs(parentfolder[0])
        except (WindowsError):
            pass
        print("URL:\t%s" % resourcehref)
        urllib.urlretrieve(resourcehref,resourcepath)
    
#start()

    

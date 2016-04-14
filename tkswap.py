#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
监测 RM09 与 RM价差变化情况.

单独线程更新global变量 price.

"""
import Tkinter as tk
import re
import urllib2
import socket
import time
import threading
price=''

url = 'http://hq.sinajs.cn/t=%s&list=' % time.time()#sina
parameter=[('RM1409','RM1501')]

class MyException(Exception):
    pass
class Timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
    def getCode(self,url):
        """
        proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
        opener=urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        #req = urllib2.urlopen(url) #wrong
        #"""
        req = urllib2.Request(url)
        try:
            fh = urllib2.urlopen(req,timeout=5)
        except socket.timeout:
            raise MyException('Timeout')
        except urllib2.URLError,e:
            raise MyException('---')
        respHtml = fh.read()
        fh.close()
        return respHtml
    def run(self):
        global price
        while not self.thread_stop:
            try:
                a=self.getPrice(url,self.processParmeter(parameter))
                
            except MyException ,e:
                price=e.message
                print(e.message+'\t'+time.strftime('%H:%M:%S'))
            time.sleep(self.interval)
    def processParmeter(self,parmeter):
        preturn = ''
        if len(parmeter)>0:
            for p in parmeter:
                preturn+=p[0]+','+p[1]+','
        return preturn
    def getPrice(self,url,parameter):
        '''
            1.get price
            2.return 差价与第一次调用时差价比较.
        '''
        global price
        resp = self.getCode(url+parameter)
        #print(resp[:-1]+" "+time.strftime('%H:%M:%S'))
        list = resp.split(";")
        result = []
        for i in range(len(list)):
            p=list[i]
            if p=='':
                pass
            pp = p.split(",")
            if len(pp)>6:
                #print(pp[7])
                result.append(pp[7])
        print(result)
        i=0
        price=''
        for i in range(0,len(result)/2):
            price = price+' '+str(int(result[2*i])-int(result[2*i+1]))
        
def updatelabel(label):
    """
    用最新price更新label显示
    """
    def update():
        label.config(text=str(price))
        label.after(100, update)#单位 毫秒
    update()

def run():
    root = tk.Tk()
    root.wm_attributes('-topmost',1)    #置顶显示
    #root.wm_overrideredirect(True)  #去掉标题等,仅仅显示label内容.
    #root.overrideredirect(True) #隐藏窗口边框与标题栏.

    #root.attributes("-transparentcolor","white")#白色透明掉.
    #root["background"] = "white"

    root.title("")
    label = tk.Label(root,text='0000')
    label.pack()
    Timer(1,10).start() #更新价格频率 单位 秒

    curWidth = root.winfo_reqwidth() # get current width
    curHeight = root.winfo_height() # get current height
    scnWidth,scnHeight = root.maxsize() # get screen width and height
    # now generate configuration information
    #tmpcnf = '%dx%d+%d+%d'%(100,10,0,scnHeight-60)#scnWidth-110#带边框位置
    tmpcnf = '%dx%d+%d+%d'%(120,10,scnWidth/2+70,scnHeight-65)#scnWidth-110#精简位置.
    #tmpcnf = '%dx%d+%d+%d'%(100,20,scnWidth/2-55,scnHeight-45)
    root.geometry(tmpcnf)
    updatelabel(label)
    root.mainloop()
run()

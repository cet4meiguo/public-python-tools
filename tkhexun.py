#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
new price of futures

单独线程更新global变量 price.

"""
import Tkinter as tk
import re
import urllib2
import socket
import time
import threading
price=''
class MyException(Exception):
    pass
class Timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
    def getCode(self,url):
        req = urllib2.Request(url)
        try:
            fh = urllib2.urlopen(req,timeout=5)
        except socket.timeout:
            raise MyException('Timeout')
        except urllib2.URLError,e:
            raise MyException('URLError')
        respHtml = fh.read()
        fh.close()
        return respHtml
    def run(self):
        global price
        while not self.thread_stop:
            try:
                #price = self.getPrice(url,parameter)#sina
                price = self.getPriceHeXun(url,parameter)#hexun
                #price = price+'\n'+self.getPriceHeXun(url,'RM1409')+'\n'+self.getPriceHeXun(url,'RB1405')#hexun
            except MyException ,e:
                price=e.message
                print(e.message+'\t'+time.strftime('%H:%M:%S'))
            time.sleep(self.interval)
    def getPrice(self,url,parameter):
        resp = self.getCode(url+parameter)
        #print(resp[:-1]+" "+time.strftime('%H:%M:%S'))
        list = resp.split(";")
        result = ''
        for i in range(len(list)):
            p=list[i]
            if p=='':
                pass
            pp = p.split(",")
            if len(pp)>6:
                if result=='':
                    result=pp[7][2:4]#+'\t'+pp[13]
                else:
                    result=result+' '+pp[7][2:4]#+'\t'+pp[13]
                """
                if result=='':
                    result=parameter.split(',')[i]+'\t'+pp[7][2:4]
                else:
                    result=result+'\n'+parameter.split(',')[i]+'\t'+pp[7][2:4]
                """
        return result
    def getPriceHeXun(self,url,parameter):
        s='http://quote.futures.hexun.com/2010/JsData/FRunTimeQuote.aspx?code=%s&market=3&&time=%s' % (parameter,time.time())
        #print(s)
        resp = self.getCode(s)
        #print(resp[:-1]+" "+time.strftime('%H:%M:%S'))
        list = resp.split(";")
        result = ''
        for i in range(len(list)):
            p=list[i]
            if p=='':
                pass
            pp = p.split(",")
            if len(pp)>6:
                if result=='':
                    result=pp[3][3:5]+' '+pp[12]
                else:
                    result=result+' '+pp[3][2:4]+' '+pp[12]
                """
                if result=='':
                    result=parameter.split(',')[i]+'\t'+pp[7][2:4]
                else:
                    result=result+'\n'+parameter.split(',')[i]+'\t'+pp[7][2:4]
                """
        return result
def updatelabel(label):
    """
    用最新price更新label显示
    """
    def update():
        label.config(text=str(price))
        label.after(500, update)#单位 毫秒
    update()

url = 'http://hq.sinajs.cn/t=%s&list=' % time.time()#sina
parameter='RM1405'


def run():
    root = tk.Tk()
    root.wm_attributes('-topmost',1)    #置顶显示
    #root.wm_overrideredirect(True)  #去掉标题等,仅仅显示label内容.
    root.title("")
    label = tk.Label(root, fg="black",text='0000')
    label.pack()
    Timer(1,10).start() #单位 秒

    curWidth = root.winfo_reqwidth() # get current width
    curHeight = root.winfo_height() # get current height
    scnWidth,scnHeight = root.maxsize() # get screen width and height
    # now generate configuration information
    tmpcnf = '%dx%d+%d+%d'%(100,10,scnWidth-110,scnHeight-60)#scnWidth-110
    #tmpcnf = '%dx%d+%d+%d'%(100,20,scnWidth/2-55,scnHeight-45)
    root.geometry(tmpcnf)
    updatelabel(label)
    root.mainloop()
run()

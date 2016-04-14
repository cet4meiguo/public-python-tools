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

url = 'http://hq.sinajs.cn/t=%s&list=' % time.time()#sina
'''
不做黑色系,不做空,不追涨杀跌,不主观交易(必须依靠图形)
趋势追踪:只顺大趋势方向做单向,在压力位置/突破(预防假突破)顺势做,同时设置保护性止损(单笔小幅度),
同时设置移动止盈,最大回撤50%止盈.然后机会来临时再度入场.
原则: 试错的成本控制,脱离成本区的盈利必须拿住最大波幅的50%.
周期,止损,都要大,1小时定方向.15分钟进场.
!不要猜测方向是否转向了,只看小时方向.不要追,要有足够的运行时间之后判断走势.
必须精细!绝对不要根据预判的大势做,自己只能做小周期,以最小的止损换取盈利.

'''
parameter='ZN1411,AG1412,P1501'     #不可修改该参数
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
    def getstockprice(self,parameter):
        #单个股票现价
        url='http://hq.sinajs.cn/?_=0.9315945492126048&list=%s' % parameter
        resp = self.getCode(url)
        return re.search(r'="(.*?)"',str(resp)).groups(1)[0].split(',')[3].split('.')[1]
    
    def run(self):
        global price
        while not self.thread_stop:
            try:
                #a = self.getfbprice()
                #a = a + ' '+self.getPrice(url,parameter)#sina
                a=self.getPrice(url,parameter)
                #b=self.getbbprice()
                #price = a+' '+b
                price=a
                #price = self.getPriceHeXun(url,parameter)#hexun
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
                #print(pp[6])
                if result=='':
                    result=pp[6][-2:]#+'\t'+pp[13]
                    if len(pp[6])<4:
                        result=pp[6][-2:]#+'\t'+pp[13]
                    else:
                        if pp[6][2]=='.':
                            result=pp[6][1:]
                        else:
                            result=pp[6][2:]#+'\t'+pp[13]
                else:
                    if len(pp[6])<4:
                        result=result+' '+pp[6][-2:]#+'\t'+pp[13]
                    else:
                        if pp[6][2]=='.':
                            result=result+' '+pp[6][1:]
                        else:
                            result=result+' '+pp[6][2:]#+'\t'+pp[13]
                """
                if result=='':
                    result=parameter.split(',')[i]+'\t'+pp[6][2:4]
                else:
                    result=result+'\n'+parameter.split(',')[i]+'\t'+pp[6][2:4]
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
                    result=parameter.split(',')[i]+'\t'+pp[6][2:4]
                else:
                    result=result+'\n'+parameter.split(',')[i]+'\t'+pp[6][2:4]
                """
        return result
    def getbbprice(self):
        #bb1409
        url='http://hq2gnqh.eastmoney.com/em_futures2010numericapplication/index.aspx?type=f&id=bb14093'
        resp = self.getCode(url)
        return re.search(r'extendedFutures:\["(.*?),',str(resp)).groups(1)[0][2:]#.split('.')[1]

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
    tmpcnf = '%dx%d+%d+%d'%(130,10,scnWidth/2-10,scnHeight-65)#scnWidth-110#精简位置.
    #tmpcnf = '%dx%d+%d+%d'%(100,20,scnWidth/2-55,scnHeight-45)
    root.geometry(tmpcnf)
    updatelabel(label)
    root.mainloop()
run()

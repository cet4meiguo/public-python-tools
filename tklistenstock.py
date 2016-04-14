#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
new price of futures
"""
import Tkinter as tk
import re
import urllib2
import socket
import time
import threading
import winsound
price=''
timeout =20
url = 'http://hq.sinajs.cn/t=%s&list=' % time.time()#sina
'''
专一 耐心 是唯一重要的事情
持戒: 不做铁矿,不追涨杀跌,剧烈波动不做,
'''
stock='sz300048'
class MyException(Exception):
    print('MyException:----'+time.strftime('%H:%M:%S'))
class Clock(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
    def time(self):
        print('Clock is running')
        """
            类似闹钟功能
        """
        s=time.gmtime(time.time())
        if(s.tm_min%3==0 and (s.tm_sec<3)):
            print(s.tm_min)
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    def run(self):
        while not self.thread_stop:
            try:
                self.time()
            except Exception,e:
                print(e.message+'\t'+time.strftime('%H:%M:%S'))
            time.sleep(self.interval)
class Timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
    def getCode(self,url):
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
    def getstockprice(self,parameter):
        print(parameter)
        #单个股票现价
        url='http://hq.sinajs.cn/list=%s' % parameter
        resp = self.getCode(url)
        print(str(resp))
        print(re.search(r'="(.*?)"',str(resp)).groups(1)[0])
        return re.search(r'="(.*?)"',str(resp)).groups(1)[0].split(',')[7]
    def time(self):
        print('Clock is running')
        #winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
        """
            类似闹钟功能
        """
        s=time.gmtime(time.time())
        print(s.tm_min)
        print(s.tm_sec)
        if(s.tm_min%2==0):
            print(s.tm_min)
            #winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            #winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    def run(self):
        
        global parameter
        #parameter = self.filterFg(parameter)    #过滤FG这个垃圾品种
        
        global price
        while not self.thread_stop:
            try:
                #self.time();
                #a = self.getfbprice()
                #a = a + ' '+self.getPrice(url,parameter)#sina
                #a=self.getPrice(url,parameter)
                b=self.getstockprice(stock)
                """
                b=self.getforex('EURGBP')
                c=self.getXAG()
                #price = a+' '+b
                #price = price+' '+c
                #"""
                price=b
                #price = self.getPriceHeXun(url,parameter)#hexun
                #price = price+'\n'+self.getPriceHeXun(url,'RM1409')+'\n'+self.getPriceHeXun(url,'RB1405')#hexun
                print(time.strftime('%H:%M:%S')+"\t"+price)
            except Exception,e:
                price='Time out'
                print(e.message+'\t'+time.strftime('%H:%M:%S'))
            time.sleep(self.interval)
    def getPrice(self,url,parameter):
        try:
            resp = self.getCode(url+parameter)
        except:
            print('error in getPrice\t'+time.strftime('%H:%M:%S'))
            raise MyException('Error')
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
    Clock(1,1).start()
    #winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    curWidth = root.winfo_reqwidth() # get current width
    curHeight = root.winfo_height() # get current height
    scnWidth,scnHeight = root.maxsize() # get screen width and height
    # now generate configuration information
    #tmpcnf = '%dx%d+%d+%d'%(100,10,0,scnHeight-60)#scnWidth-110#带边框位置
    tmpcnf = '%dx%d+%d+%d'%(160,10,scnWidth/2-80,scnHeight-62)#scnWidth-110#精简位置.
    #tmpcnf = '%dx%d+%d+%d'%(100,20,scnWidth/2-55,scnHeight-45)
    root.geometry(tmpcnf)
    updatelabel(label)
    root.mainloop()
run()

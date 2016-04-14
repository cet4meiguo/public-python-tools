#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
new price of futures
"""
import re
import urllib2
import socket
import time
import threading

price=''

url = 'http://hq.sinajs.cn/t=%s&list=' % time.time()#sina
'''
经:
D1,Min M15
BEN
整劲

'''

parameter='PP1609,I1609,RB1610'
forex='EURGBP'
stock='sz300048,sh600871'
#parameter='L1505'
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
        proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
        opener=urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        #req = urllib2.urlopen(url) #wrong
        #"""
        req = urllib2.Request(url)
        try:
            fh = urllib2.urlopen(req,timeout=5)
        except socket.timeout:
            print('error in getcode')
            raise MyException('Timeout')
        except urllib2.URLError,e:
            print('error in getcode')
            raise MyException('---')
        except Exception:
            raise MyException('Exception')
        try:
            respHtml = fh.read()
        except:
            print('error in getcode')
            raise MyException('---')
        fh.close()
        return respHtml
    def getstockprice(self,parameter):
        print(parameter)
        #单个现价
        url='http://hq.sinajs.cn/list=%s' % parameter
        resp = self.getCode(url)
        #print(str(resp))
        list = resp.split(";\n")[:-1]
        result = ''
        print(len(list))
        for i in list:
            if i=='':
                pass
            #print('i:%s'%i)
            #print(re.search(r'="(.*?)"',str(i)).groups(1)[0])
            p= (re.search(r'="(.*?)"',str(i)).groups(1)[0]).split(',')[7][0:5]
            result +=' '+p
        return result
    def getforex(self,parameter):
        url='http://hq.sinajs.cn/?rn=1420679359382&list=%s' % parameter
        try:
            resp = self.getCode(url)
        except:
            print('error in getforex\t'+time.strftime('%H:%M:%S'))
            raise MyException('Error')
        return re.search(r'="(.*?)"',str(resp)).groups(1)[0].split(',')[8][2:]
    def getXAG(self):
        url='http://quote.forex.hexun.com/2010/Data/FRunTimeQuote.ashx?code=XAGUSD'
        try:
            resp = self.getCode(url)
        except:
            print('error in getforex\t'+time.strftime('%H:%M:%S'))
            raise MyException('Error')
        return re.search(r'=\[(.*?)\]',str(resp)).groups(1)[0].split(',')[2][0:]
    def filterFg(self,p):
        #partten = re.compile(r'FG\d\d\d\d')
        #p=partten.sub(r'',p)
        return p
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
            #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
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
                a=self.getPrice(url,parameter)
                #b=self.getstockprice(stock)
                """
                b=self.getforex('EURGBP')
                c=self.getXAG()
                #price = a+' '+b
                #price = price+' '+c
                #"""
                #price=a+' '+b
                price=a
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
        for i in range(len(list)):#-1,最后为hf_XAU
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
        #return result+" "+list[len(list)-2][22:27]
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




Timer(1,10).start() #更新价格频率 单位 秒



#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
futures tool
"""
import Tkinter as tk
import re
import urllib2
import time

def getCode(url):
    req = urllib2.Request(url)
    fh = urllib2.urlopen(req)
    respHtml = fh.read()
    fh.close()
    return respHtml
def getmatch(url,parameter):
    resp = getCode(url+parameter)
    print(resp)
    list = resp.split(";")
    result = []
    for p in list:
        if p=='':
            pass
        pp = p.split(",")
        if len(pp)>6:
            result.append(p.split(",")[7])
    return result
url = 'http://hq.sinajs.cn/list='
parameter='RM1401,M1405'

def counter_label(label):
    def count():
        price=''
        try:
            prices = getmatch(url,parameter)
        except:
            prices=['Error','Error']
        for p in prices:
            if price=='':
                price=p
            else:
                price=price+'\n'+p
        label.config(text=str(price))
        label.after(10000, count)
    count()
class App():
    def __init__(self):
        self.root=tk.Tk()

        self.menu = tk.Menu(self.root)
        self.menu.add_command(label='Set',command=self.menu)
        self.root['menu']=self.menu

        self.menu2=tk.Menu(self.root)
        self.mainmenu = tk.Menu(self.menu2,tearoff=0)
        for item in ['Python','Java']:
            self.mainmenu.add_command(label=item,command=self.menu)
        self.menu2.add_cascade(label='Language',menu=self.menu2)
        self.root['menu']=self.menu2
        
        self.label=tk.Label()
        self.label.pack()
        self.update()

        self.canvas=tk.Canvas(width=600,height=400,bg='white')
        self.canvas.pack()
        
        self.root.mainloop()
    def menu(self):
            pass
    def update(self):
        now=time.strftime('%H:%M:%S')
        self.label.config(text=now)
        self.label.after(1000,self.update)
app = App()
app.mainloop()
def run():
    root = tk.Tk()
    root.wm_attributes('-topmost',1)    #置顶显示
    #root.wm_overrideredirect(True)  #去掉标题等,仅仅显示label内容.
    root.title("")
    label = tk.Label(root, fg="black")
    label.pack()
    counter_label(label)
    root.mainloop()



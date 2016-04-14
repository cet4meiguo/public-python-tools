#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
Tkinter Button
"""
from Tkinter import *
def helloButton():
    print('hello button')

root = Tk()
Button(root,text='Hello Button',command=helloButton).pack()
Button(root,text='FLAT',relief=FLAT).pack()
Button(root,text='GROOVE',relief=GROOVE).pack()
Button(root,text='RAISED',relief=RAISED).pack()
Button(root,text='SOLID',relief=SOLID).pack()
Button(root,text='SUNKEN',relief=SUNKEN).pack()
"""
bitmap = BitmapImage(file='e:/dropbox/bitmap.gif')
Button(root,bitmap=bitmap).pack()
"""

BITMAP = """

"""
#bp=BitmapImage(data=BITMAP)
#Button(root,bitmap=bp).pack()

def call1():
    print('button1')
def call2(event):
    print('event.time=%s'% event.time)
    print('event.type=%s' % event.type)
    print('event.WidgetId=%s'% event.widget)
    print('event.KeySymbol=%s'% event.keysym)
def call3():
    print('button3')
b1=Button(root,text='button1',command=call1)
b2=Button(root,text='button2')
b2.bind('<Return>',call2)
b2.bind('<Enter>',call2)
b3=Button(root,text='button3',command=call3)
b1.pack()
b2.pack()
b3.pack()

b2.focus_set()

b3 = Button(root,text='button1',width=30,height=1)
b3.pack()
b4=Button(root,text='button2')
b4['width']=30
b4['height']=2
b4.pack()
b5=Button(root,text='button3')
b5.configure(width=30,height=3)
b5.pack()

for d in[0,1,2,3]:
    Button(root,text=str(d),bd=d).pack()

for status in ['normal','active','disabled']:
    Button(root,text=status,state=status,width=30).pack()

def changeText():
    if b['text']=='text':
        v.set('change')
    else:
        v.set('text')
v=StringVar()
b=Button(root,textvariable=v,command=changeText)
v.set('text')
b.pack()
root.mainloop()

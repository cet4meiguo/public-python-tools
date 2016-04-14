#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
Tkinter Label
"""
from Tkinter import *
root = Tk()
root.title('Label')

label = Label(root,text='Hello Tkinter')
label.pack()

label2=Label(root,bitmap='error')
label2.pack()

label3=Label(root,bitmap='info')
label3.pack()

label4=Label(root,bitmap='question')
label4.pack()

label5=Label(root,bitmap='warning')
label5.pack()

label6=Label(root,bitmap='gray12')
label6.pack()

#label7=Label(root,PhotoImage(file='e:/dropbox/love.jpg'))
#label7.pack()

"""
bitmap = BitmapImage(file='e:/dropbox/bitmap.bmp')
label8=Label(root,bitmap=bitmap)
label8.bm = bitmap
label8.pack()
"""

label9 = Label(root,bg='white',fg='black',width=20,height=10,text='color')
label9.pack()

label10 = Label(root,text='left',bitmap='error',compound='left')
label10.pack()
label11 = Label(root,text='center',bitmap='error',compound='center')
label11.pack()
"""
anchor:
nw        n      ne
w       center   e
sw        s      se
"""
label12=Label(root,text='啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',width=20,height=10,
              wraplength=120,justify='left',anchor='w',bg='white',fg='black')
label12.pack()

root.mainloop()


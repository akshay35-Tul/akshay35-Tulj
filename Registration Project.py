#!/usr/bin/env python
# coding: utf-8

# In[21]:


import tkinter as Tk
from tkinter import *
import tkinter


# In[54]:


top=Tk()

top.title("Data Science")
top.geometry("1200x800+0+0")
top.configure(background="powderblue")

def func():
    n=name.get()
    print(n)


tkinter.Label(top, text="Today's Visitor", font=('times',20,'bold'),height='1', width='13').grid(row=0, column=0, sticky=W)

tkinter.Label(top, text="0", bg="orange",font=('times',20,'bold'),height='1', width='4').grid(row=0, column=2, sticky=W)

tkinter.Label(top, text="Today's Visitor", font=('times',20,'bold'),height='1', width='13').grid(row=0, column=4, sticky=W)

tkinter.Canvas(top, width="1200", height="2", bg='black').grid(row=1, columns=8)

tkinter.Label(top, text=" ").grid(row=2, column=0, sticky=W)


tkinter.Label(top, text="Name",bg="powderblue",fg="black").grid(row=3, column=1,sticky=E)
name=StringVar()
tkinter.Entry(top, width=40,textvariable="name", bg="white").grid(row=3, column=2,sticky=E)

tkinter.Label(top, text="Place",bg="powderblue",fg="black").grid(row=4, column=1,sticky=E)
place=StringVar()
tkinter.Entry(top, width=40, textvariable="place",bg="white").grid(row=4, column=2,sticky=E)

tkinter.Label(top, text="Mobile",bg="powderblue",fg="black").grid(row=5, column=1,sticky=E)
mobile=StringVar()
tkinter.Entry(top, width=40, textvariable="mobile",bg="white").grid(row=5, column=2,sticky=E)

tkinter.Label(top, text="Email ID",bg="powderblue",fg="black").grid(row=6, column=1,sticky=E)
email=StringVar()
tkinter.Entry(top, textvariable="email",width=40, bg="white").grid(row=6, column=2,sticky=E)

tkinter.Label(top, text="Date",bg="powderblue",fg="black").grid(row=7, column=1,sticky=E)
date=StringVar()
tkinter.Entry(top, textvariable="date",width=40, bg="white").grid(row=7, column=2,sticky=E)

tkinter.Label(top, text="Time",bg="powderblue",fg="black").grid(row=8, column=1,sticky=E)
time=StringVar()
tkinter.Entry(top, textvariable="time",width=40, bg="white").grid(row=8, column=2,sticky=E)

tkinter.Label(top, text="Purpose",bg="powderblue",fg="black").grid(row=9, column=1,sticky=E)
purpose=StringVar()
tkinter.Entry(top, textvariable="purpose",width=40, bg="white").grid(row=9, column=2,sticky=E)

tkinter.Button(top, text="Save/Print").grid(row=10, column=1, sticky=E)
tkinter.Button(top, text="Clear").grid(row=10, column=2, sticky=E)

cap=Button(top, text="capture").grid(row=11, column=4, sticky=E)
img1=tkinter.PhotoImage(file="C:\\Users\\cadd\\Contacts\\Desktop\\download.png")
Label(top, image=img1, height="145", width="125", borderwidth=2, relief='solid').grid(row=3,rows=5, column=4, columns=1 ,sticky=E)


# In[55]:


top.mainloop()


# In[ ]:





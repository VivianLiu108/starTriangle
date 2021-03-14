# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:39:50 2021

@author: 108321025
"""

from tkinter import*
root=Tk()
root.title("stars")
starnum=10
stars=""
for i in range (1,starnum):
    stars+="*"*i
    if i!=starnum-1:
        stars+="\n"
label=Label(root,text=stars,font=("Courier New",15,"bold"))
label.pack()
stars=""
for i in range (1,starnum):
    stars+="*"*i
    if i!=starnum-1:
        stars+="\n"
label2=Label(root,text=stars,justify="left",font=("Courier New",15,"bold"),padx=1)
label2.pack()
root.mainloop()
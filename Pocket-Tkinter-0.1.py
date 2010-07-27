#-*- coding:utf-8-*-
from Tkinter import *
from tkMessageBox import *
from FileDialog import *
import os

#fileload=LoadFileDialog(root)
#filepath=fileload.go()
#filepathname=os.path.dirname(filepath)
MainWindow=Tk()
MainWindow.title("Pocket Tkinter 0.1")
MainWindow.resizable(width=FALSE,height=FALSE)
MainWindow.geometry("230x250")
img1=PhotoImage(file='/ptkimages/newwindow.gif')
def newwindow():
    NewWindow=Toplevel()
    NewWindow.title("新建窗体")
    NewWindow.resizable(width=FALSE,height=FALSE)
    NewWindow.geometry("210x200")

    Label(NewWindow,text="标题：").place(relx=0.0,rely=0.0,relwidth=0.22,relheight=0.06)
    Label(NewWindow,text="高度：").place(relx=0.0,rely=0.1,relwidth=0.22,relheight=0.06)
    Label(NewWindow,text="宽度：").place(relx=0.0,rely=0.2,relwidth=0.22,relheight=0.06)
    Label(NewWindow,text=" 无框窗口：").place(relx=0.0,rely=0.3,relwidth=0.3,relheight=0.06)

    entrywtitle=StringVar()
    entrywtitle.set("From 1")
    newwindowname=Entry(NewWindow,textvariable=entrywtitle).place(relx=0.2,rely=0.0,relwidth=0.7,relheight=0.08)

    entryheight=StringVar()
    entryheight.set("158")
    newwindowheight=Entry(NewWindow,textvariable=entryheight).place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.08)

    entrywidth=StringVar()
    entrywidth.set("207")
    newwindowwidth=Entry(NewWindow,textvariable=entrywidth).place(relx=0.2,rely=0.2,relwidth=0.7,relheight=0.08)
    changeckk=StringVar()
    Checkbutton(NewWindow,variable=changeckk,onvalue='True',offvalue='False').place(relx=0.33,rely=0.3,relwidth=0.22,relheight=0.06)

    def donewwindow():
        dowmwindowini=open(filepathname+"//sys//mainwindow//title.txt","w")
        dowmwindowini.write(entrywtitle.get())
        dowmwindowini.close()
        dowmwindowini=open(filepathname+"//sys//mainwindow//height.txt","w")
        dowmwindowini.write(entryheight.get())
        dowmwindowini.close()
        dowmwindowini=open(filepathname+"//sys//mainwindow//width.txt","w")
        dowmwindowini.write(entrywidth.get())
        dowmwindowini.close()
        if changeckk.get()=="":
            dowmwindowini=open(filepathname+"//sys//mainwindow//overrideredirect.txt","w")
            dowmwindowini.write("False")
            dowmwindowini.close()
        else:
            dowmwindowini=open(filepathname+"//sys//mainwindow//overrideredirect.txt","w")
            dowmwindowini.write(changeckk.get())
            dowmwindowini.close()
        
        NewWindow.destroy()
    
    Button(NewWindow,text="确定",command=donewwindow).place(relx=0.0,rely=0.89,relwidth=0.4,relheight=0.1)
    Button(NewWindow,text="取消",command=NewWindow.destroy).place(relx=0.6,rely=0.89,relwidth=0.4,relheight=0.1)
    NewWindow.mainloop()

Button(image=img1,command=newwindow).place(relx=0.0,rely=0.89,relwidth=0.22,relheight=0.07)
MainWindow.mainloop()

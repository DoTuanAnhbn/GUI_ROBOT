from tkinter import *
import tkinter
from PIL import Image,ImageTk
import cv2

window  = Tk()
window.geometry("700x450")
window.maxsize(700,450)
window.minsize(700,450)
window.title("GUI Control")

#Command

def Command_bt6():
    lb7.configure(text="CONNECT",font=("arial",14),bg="green")
    return

def Command_bt7():
    lb7.configure(text="DISCONNECT",font=("arial",14),bg="red")
    return

#Label

lb1=tkinter.Label(text="MENU CONTROL",fg="white",bg="green",font=("time new roman",18),padx="10",pady="4")
lb1.pack()

lb2=tkinter.Label(text='IP',bg="yellow",font=("arial",14),padx=18)
lb2.place(x=50,y=50)

lb3=tkinter.Label(text='PORT',bg="yellow",font=("arial",14))
lb3.place(x=50,y=100)

lb4=tkinter.Label(text='STATUS',bg="yellow",font=("arial",14))
lb4.place(x=50,y=150)

lb4=tkinter.Label(text="LED",bg="yellow",font=("arial",14),padx=8)
lb4.place(x=550,y=50)

lb5=tkinter.Label(bg="orange",height=14,width=30)
lb5.place(x=295,y=70)

lb6=tkinter.Label(text='Speed',bg="yellow",font=("arial",14),padx=12)
lb6.place(x=100,y=200)

lb7=tkinter.Label()
lb7.place(x=150,y=150)

#Button

img1=Image.open("left.png")
resize1=img1.resize( (50,50),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(resize1)
bt1=tkinter.Button(window,image=photo1)
bt1.place(x=300,y=150)

img2=Image.open("right.png")
resize2=img2.resize( (50,50),Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(resize2)
bt2=tkinter.Button(window,image=photo2)
bt2.place(x=450,y=150)

img3=Image.open("up.png")
resize3=img3.resize( (50,50),Image.ANTIALIAS)
photo3=ImageTk.PhotoImage(resize3)
bt3=tkinter.Button(window,image=photo3)
bt3.place(x=375,y=75)

img4=Image.open("down.png")
resize4=img4.resize( (50,50),Image.ANTIALIAS)
photo4=ImageTk.PhotoImage(resize4)
bt4=tkinter.Button(window,image=photo4)
bt4.place(x=375,y=225)

img5=Image.open("stop.jpg")
resize5=img5.resize( (50,50),Image.ANTIALIAS)
photo5=ImageTk.PhotoImage(resize5)
bt5=tkinter.Button(window,image=photo5)
bt5.place(x=375,y=150)

bt6=tkinter.Button(window,text="CONNECT",font=("arial",14),bg="green",command=Command_bt6)
bt6.place(x=275,y=325)

bt7=tkinter.Button(window,text="DISCONNECT",font=("arial",14),bg="red",command=Command_bt7)
bt7.place(x=400,y=325)

bt8=tkinter.Button(window,text='Slow',font=("arial",14),padx=15,bg="gray")
bt8.place(x=100,y=250)

bt9=tkinter.Button(window,text='Balance',font=("arial",14),bg="gray")
bt9.place(x=100,y=300)

bt10=tkinter.Button(window,text='Fast',font=("arial",14),padx=16,bg="gray")
bt10.place(x=100,y=350)

bt11=tkinter.Button(window,text='ON',font=("arial",14),bg="green",padx=7)
bt11.place(x=550,y=100)

bt12=tkinter.Button(window,text='OFF',font=("arial",14),bg="red")
bt12.place(x=550,y=150)

#Entrybox

txt1=tkinter.Entry(font=("arial",12),width=15)
txt1.place(x=150,y=55)

txt2=tkinter.Entry(font=("arial",12),width=15)
txt2.place(x=150,y=105)











window.mainloop()
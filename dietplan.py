from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkinter import PhotoImage

from PIL import Image,ImageTk
win= Tk()
win.title('DietPlan')
win.geometry("900x500")



def exit1():
   win.destroy()
   import normalweight


Label(win, text = 'Choose your Diet Plan:', font =('Arial 30 bold')).place(x =0,y = 50)
button1= tk.Button(win,text='Diet Plan For NormalWeight',font= ('Helvetica 15 bold'), compound= TOP, command=exit1)
button1.pack(side='top')
button1.place(x=350,y=200)





def exit():
   win.destroy()
   import underweight

button2= tk.Button(win,text='Diet Plan For Underweight',font= ('Helvetica 15 bold'), compound= BOTTOM, command=exit)
button2.pack(side='bottom')
button2.place(x=350,y=250)


def exit2():
   win.destroy()
   import overweight


Label(win, text = 'Choose your Diet Plan:', font =('Arial 30 bold')).place(x =0,y = 50)
button1= tk.Button(win,text='Diet Plan For Overweight',font= ('Helvetica 15 bold'), compound= TOP, command=exit2)
button1.pack(side='top')
button1.place(x=350,y=300)






win.mainloop()

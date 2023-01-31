from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkinter import PhotoImage
import textwrap
from PIL import Image,ImageTk
win= Tk()
win.title('DietPlan')
win.geometry("2560x1600")



wrapper = textwrap.TextWrapper(width=50)
  
  

Label(win, text = 'Tips to get fit from normal', font =('Arial 30 bold')).place(x =0,y = 50)
Label(win, text = 'Tasks to be done:', font =('Arial 30 bold')).place(x =60,y = 550)

Label(win,text="""Increase calorie intake: Make sure you're consuming enough calories to support muscle growth.\n
Lift heavy weights: Focus on compound exercises such as squats, deadlifts, and bench press, and gradually increase the weight you lift.\n
Eat enough protein: Aim for at least 0.8 grams of protein per pound of body weight per day.\n
Get enough rest: Sleep is crucial for muscle recovery and growth. \n
Aim for at least 7-9 hours of sleep per night.\n
Be consistent: Stick to a workout and nutrition plan, and make adjustments as needed.\n
Consider hiring a personal trainer or coach who can help you customize a workout plan specifically for you.\n
Avoid excessive cardio as this may burn muscle mass.\n
Be patient, building muscle takes time, don't get discouraged if you don't see results right away.\n""",font=('arial 15 bold')).place(x=50,y=100)









def exit():
    win.destroy()
    import dietplan

b2=tk.Button(win,text="Back",font=("Arial",13),bg='lightgreen',command=exit)
b2.grid(row=2, column=1)










  
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()


  
Button1 = Checkbutton(win, text = "drink 8l of water",font='arial 15 bold')
  
Button2 = Checkbutton(win, text = "workout an 1hour",font='arial 15 bold')
  
                     
Button3 = Checkbutton(win, text = "took high caloire food",font='arial 15 bold')
  
                     

                     
    
Button1.place(x=60,y=600)  
Button2.place(x=60,y=630)  
Button3.place(x=60,y=660)


  
  


win.mainloop()

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
  
  

Label(win, text = 'Tips to gain weight:', font =('Arial 30 bold')).place(x =0,y = 50)
Label(win, text = 'Tasks to be done:', font =('Arial 30 bold')).place(x =60,y = 550)

Label(win,text="""Use calorie-dense foods: Eating calorie-dense foods such as nuts, seeds, avocado, and dried fruits can help increase calorie intake without feeling overly full.\n

Drink calorie-containing beverages: Drinking calorie-containing beverages such as smoothies, milkshakes, and protein shakes can help increase calorie intake.\n

Be sure to use ingredients such as full-fat dairy, nut butter, and avocado to make them more calorie-dense.\n

Cook with healthy oils: Cooking with healthy oils such as olive oil, coconut oil, and avocado oil can add extra calories to meals.\n

Add calorie-dense toppings: Adding calorie-dense toppings such as cheese, sour cream, and guacamole to meals can increase calorie intake.\n

Take weight gain supplements: Weight gain supplements such as protein powders, weight gainers, and creatine can help increase calorie intake and promote muscle growth.\n
However, it is important to consult with a healthcare professional before starting any supplements.\n

Avoid Crash dieting: Crash dieting or skipping meals can slow down the metabolism and make it harder to gain weight.\n

Instead, focus on eating nutrient-dense foods and increasing overall calorie intake in a healthy and sustainable way.""",font=('arial 15 bold')).place(x=10,y=100)


  
  
  
def exit():
    
    win.destroy()
    import dietplan
    

b2=tk.Button(win,text="Back",font=("Arial",13),bg='lightgreen',command=exit)
b2.grid(row=2, column=1)


  
  
  
  
  
  
  
  
  
  
  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()  
Checkbutton5 = IntVar()  

  
  
Button2 = Checkbutton(win, text = "drink 8l of water.",font='arial 15 bold')
  
                     
Button3 = Checkbutton(win, text = "workout an 1hour",font='arial 15 bold')
  
                     
Button4 = Checkbutton(win, text = "took high caloire food",font='arial 15 bold')
  
                       
Button5 = Checkbutton(win, text = "track your steps",font='arial 15 bold')
  
                     

                     
    
Button2.place(x=60,y=630)  
Button3.place(x=60,y=660)
Button4.place(x=60,y=690)
Button5.place(x=60,y=720)

  
  


win.mainloop()

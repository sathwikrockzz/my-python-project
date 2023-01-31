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
  
  

Label(win, text = 'Tips to loose weight:', font =('Arial 30 bold')).place(x =0,y = 50)

Label(win,text="""Create a calorie deficit: To lose weight, you need to burn more calories than you consume.\n Keep track of your daily calorie intake and make sure it's lower than the number of calories you burn through exercise and daily activities.\n

Eat nutrient-dense foods: Focus on eating whole, unprocessed foods like fruits, vegetables, lean proteins, and whole grains.\n Avoid processed foods, sugary drinks and high-calorie snacks.\n

Incorporate regular physical activity: Aim for at least 150 minutes of moderate-intensity exercise or 75 minutes of vigorous-intensity exercise per week,\n as well as muscle-strengthening activities at least twice per week.\n

Get enough sleep: Aim for 7-9 hours of sleep per night, as poor sleep is linked to weight gain.\n

Avoid eating late at night: Eating late in the evening can lead to weight gain and disrupts your sleep.\n

Drink water: Drinking water before meals can help control your appetite and reduce your calorie intake.\n

Avoid stress: Stress can lead to overeating and weight gain. Try to find healthy ways to manage stress, such as yoga or meditation.\n

Keep track of your progress: Keep track of your weight, body measurements and progress pictures. \n This will help you to stay motivated and make adjustments as needed.\n

Consider working with a registered dietitian or nutritionist who can help you develop a personalized weight loss plan.\n""",font=('arial 15 bold')).place(x=10,y=100)


  
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()  
Checkbutton5 = IntVar()  
Checkbutton6 = IntVar()
Checkbutton7 = IntVar()  

  
Button1 = Checkbutton(win, text = "Tutorial",font='arial 15 bold')
  
Button2 = Checkbutton(win, text = "Student",font='arial 15 bold')
  
                     
Button3 = Checkbutton(win, text = "Courses",font='arial 15 bold')
  
                     
Button4 = Checkbutton(win, text = "Courses",font='arial 15 bold')
  
                       
Button5 = Checkbutton(win, text = "Courses",font='arial 15 bold')
  
                     
Button6 = Checkbutton(win, text = "Courses",font='arial 15 bold')
  
                      
    
Button7 = Checkbutton(win, text = "Courses",font='arial 15 bold')
  
                     
    
Button1.place(x=60,y=600)  
Button2.place(x=60,y=630)  
Button3.place(x=60,y=660)
Button4.place(x=60,y=690)
Button5.place(x=60,y=720)
Button6.place(x=60,y=750)
Button7.place(x=60,y=780)

  
  


win.mainloop()

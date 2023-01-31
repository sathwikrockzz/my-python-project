from tkinter import *
import tkinter as tk
from tkinter import PhotoImage

from PIL import Image,ImageTk
win= Tk()
win.title('Gender')
win.geometry("900x500")
def close_win():
   win.destroy()
   import age
   
 
# Create label
Label(win, text = 'Select your gender', font =('Arial 20 bold')).pack(side = TOP, pady =150,padx = 350) 

#Load the image
image1 = Image.open('male.jpeg')
#Resize the Image
image1 = image1.resize((80,80), Image.ANTIALIAS)
#Convert the image to PhotoImage
img1= ImageTk.PhotoImage(image1)
#Create a Label
#Create a label with the image
button1= tk.Button(win,font= ('Helvetica 15 bold'),image=img1, compound= RIGHT, command=close_win)
button1.pack(side='left')
button1.place(x=350,y=200)


def close_win():
   win.destroy()
   import age

image2 = Image.open('female.jpeg')
#Resize the Image
image2= image2.resize((80,80), Image.ANTIALIAS)
#Convert the image to PhotoImage
img2= ImageTk.PhotoImage(image2)
#Create a Label
#Create a label with the image
button2= tk.Button(win,font= ('Helvetica 15 bold'),image=img2, compound= LEFT, command=close_win)
button2.pack(side='right')
button2.place(x=450,y=200)




win.mainloop()


import tkinter as tk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from itertools import count, cycle
import time
import threading

class ImageLabel(tk.Label):
    count=0
   
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
        self.count=1
 
    def unload(self):
        self.config(image=None)
        self.frames = None
        root.destroy()
        import myproject
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
           
 
#demo :
root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('applogovideo.gif')
#start_time = threading.Timer(2,lbl.unload)
#start_time.start()

def window_main():
    root.destroy()
    import myproject
    
root.after(1500 , window_main)
    






root.mainloop()




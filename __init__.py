from tkinter import *
from library import *
from book import *

w = Tk()
welcome_msg='''Your Library
Welcome!!'''
greeting = Label(text=welcome_msg, foreground="#0032aa", background="#ffaadf",
                 width=100, height=5)
greeting.pack()
w.mainloop()

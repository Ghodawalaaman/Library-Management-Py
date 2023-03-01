from tkinter import *
# from library import *
from book import *

b1 = Book(name="book1", author="xyz", quantity=32)
b1.display()

w = Tk()
welcome_msg='''Your Library
Welcome!!'''
greeting = Label(text=welcome_msg, foreground="#0032aa", background="#ffaadf",
                 width=100, height=5)
# greeting.grid(row=0,column=1)
for i in range(3):
    for j in range(3):
        frame = Frame(
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
w.mainloop()

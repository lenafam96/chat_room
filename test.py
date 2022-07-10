from tkinter import *

win = Tk()

win.geometry("700x250")


def click(event):
    name.configure(state=NORMAL)
    name.delete(0, END)
    name.unbind('<Button-1>', clicked)


label = Label(win, text="Enter Your Name", font=('Helvetica 13 bold'))
label.pack(pady=10)

name = Entry(win, width=45)
name.insert(0, 'Enter Your Name Here...')
name.pack(pady=10)

clicked = name.bind('<Button-1>', click)
win.mainloop()

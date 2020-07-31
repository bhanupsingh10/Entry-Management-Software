import PIL.ImageTk, PIL.Image
import tkinter
from tkinter import *
import tkinter.messagebox
from twilio.rest import Client
from check_out import *

def checkout_screen():

    window = Tk()
    window.geometry("500x450")  # setting size of the window
    window.title("Entry Management Software")  # title of the window
    window.configure(background="light blue")
    window.resizable(0, 0)  # making the window non-resizable

    label1 = Label(window, text="Check Out", fg='indigo', bg='light blue', font=("comic sans ms", 18, "bold"))
    label1.place(x=40, y= 215 )

    label2 = Label(window, text="Visitor's Email", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label2.place(x=60, y=270)

    entry_1 = Entry(window)
    entry_1.place(x=270, y=270)

    button1 = Button(window, text="   Check Out  ", fg='black', bg='white',
                     command=lambda: check_out1(entry_1), relief=RIDGE,
                     activebackground='grey',font=("arial", 12, "bold"))
    button1.place(x=180, y=320)

    # adding logo(image) of the company
    path = r"E:\Placement\Projects\Entry Management\bg.png"  # path where image is stored
    img = PIL.ImageTk.PhotoImage(PIL.Image.open(path))
    panel = Label(window, image=img)
    panel.place(x=40, y=5)
    window.mainloop()
    window.mainloop()
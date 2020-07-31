import PIL.ImageTk, PIL.Image
import tkinter
from tkinter import *
import tkinter.messagebox
from twilio.rest import Client
from check_in import *
from check_out import*

#Home Page of the Graphical User Interface
def home_screen():

    window = Tk()
    window.geometry("500x650")                          #setting size of the window
    window.title("Entry Management Software")           #title of the window
    window.configure(background="light blue")
    window.resizable(0, 0)                              #making the window non-resizable

    #placing labels and entry fields in the GUI
    label1 = Label(window, text="VISITOR DETAILS", fg='indigo', bg='light blue', font=("comic sans ms", 18, "bold"))
    label1.place(x=40,y= 215)

    label2 = Label(window, text="Visitor's Name", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label2.place(x=60, y=265)

    entry_1 = Entry(window)
    entry_1.place(x=270, y=265)

    label3 = Label(window, text="Visitor's Email", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label3.place(x=60, y=295)

    entry_2 = Entry(window)
    entry_2.place(x=270, y=295)

    label4 = Label(window, text="Visitor's Mobile No.", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label4.place(x=60, y=325)

    entry_3 = Entry(window)
    entry_3.place(x=270, y=325)

    label5 = Label(window, text="HOST DETAILS", fg='indigo', bg='light blue', font=("comic sans ms", 18, "bold"))
    label5.place(x=40, y=365)

    label6 = Label(window, text="Host's Name", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label6.place(x=60, y=405)

    entry_4 = Entry(window)
    entry_4.place(x=270, y=405)

    label7 = Label(window, text="Host's Email", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label7.place(x=60, y=435)

    entry_5 = Entry(window)
    entry_5.place(x=270, y=435)

    label8 = Label(window, text="Host's Mobile No.", fg='blue', bg='light blue', width=15, font=("arial", 12))
    label8.place(x=60, y=465)

    entry_6 = Entry(window)
    entry_6.place(x=270, y=465)

    #adding button for further functioning
    button1 = Button(window, text="   Check In  ", fg='black', bg='white',activebackground='grey',
                        command= lambda: check_in(entry_1,entry_2,entry_3,entry_4,entry_5,entry_6),
                        relief=RIDGE,font=("arial", 14, "bold"))
    button1.place(x=70, y=520)

    button2 = Button(window, text=" Check Out ", fg='black', bg='white',activebackground='grey',
                        command=checkout_screen,
                       relief=RIDGE, font=("arial", 14, "bold"))
    button2.place(x=270, y=520)

    #adding logo(image) of the company
    path = r"E:\Placement\Projects\Entry Management\bg.png"         #path where image is stored
    img = PIL.ImageTk.PhotoImage(PIL.Image.open(path))
    panel = Label(window, image=img)
    panel.place(x=40,y=5)
    window.mainloop()
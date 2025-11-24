import tkinter
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=10)
entry.focus()
entry.grid(column=5,row=0)

label = Label(text="Miles")
label.config(padx=5)
label.grid(column=6, row=0)

label2 = Label(text="is equal to")
label2.grid(column=4, row=1)

label3 = Label(text="")
label3.grid(column=5, row=1)

label4 = Label(text="Km")
label4.config(padx=5)
label4.grid(column=6, row=1)

def action():
    km_value =  str(1.609344 * float(entry.get()))
    label3.config(text= km_value)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=5, row=3)


window.mainloop()
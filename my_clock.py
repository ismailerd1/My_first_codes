from tkinter import *
from time import *

def update():
    time_now = strftime("%H.%M.%S")
    time_label.config(text=time_now)

    date_now = strftime("%D")
    date_label.config(text=date_now)
    main.after(1000,update)

main = Tk()
main.title("Current Time")
main.geometry("200x200")
main.configure(bg="black")

time_label = Label(font=("Helvetica", 20, "bold"), fg="green",bg="black")
time_label.pack()

date_label = Label(font=("Helvetica", 20, "bold"), fg="green",bg="black")
date_label.pack()

update()

main.mainloop()
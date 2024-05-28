from tkinter import *


def press_number(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""



window = Tk()
window.title("Calculator")
#window.geometry("400x400")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.grid()

btn_frame = Frame(window)
btn_frame.grid()

button1 = Button(btn_frame, text="1",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(1))
button1.grid(row=1, column=1)
button2 = Button(btn_frame, text="2",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(2))
button2.grid(row=1, column=2)
button3 = Button(btn_frame, text="3",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(3))
button3.grid(row=1, column=3)
button4 = Button(btn_frame, text="4",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(4))
button4.grid(row=2, column=1)
button5 = Button(btn_frame, text="5",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(5))
button5.grid(row=2, column=2)
button6 = Button(btn_frame, text="6",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(6))
button6.grid(row=2, column=3)
button7 = Button(btn_frame, text="7",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(7))
button7.grid(row=3, column=1)
button8 = Button(btn_frame, text="8",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(8))
button8.grid(row=3, column=2)
button9 = Button(btn_frame, text="9",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(9))
button9.grid(row=3, column=3)
button0 = Button(btn_frame, text="0",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number(0))
button0.grid(row=4, column=2)

button_plus = Button(btn_frame,text="+",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number("+"))
button_plus.grid(row=1,column=4)
button_abs = Button(btn_frame, text="-",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number("-"))
button_abs.grid(row=2,column=4)
button_mul = Button(btn_frame, text="x",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number("*"))
button_mul.grid(row=3,column=4)
button_div = Button(btn_frame, text="/",font=("calibri",10),bg="grey",width=8, height=4, command=lambda:press_number("/"))
button_div.grid(row=4,column=4)
button_clear = Button(btn_frame, text="clear",font=("calibri",10),bg="grey",width=8, height=4, command=clear)
button_clear.grid(row=4,column=1)
button_equal = Button(btn_frame, text="=",font=("calibri",10),bg="grey",width=8, height=4, command=equals)
button_equal.grid(row=4,column=3)


window.mainloop()
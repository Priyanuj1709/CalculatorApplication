from tkinter import *

window = Tk()
window.geometry('500x500')

# clear box
e = Entry(window, width=81, borderwidth=5)
e.place(x=0, y=0)


# Functions
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)


def subtract():
    n1 = e.get()
    global math
    math = 'subtraction'
    global i
    i = int(n1)
    e.delete(0, END)


def multiply():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i = int(n1)
    e.delete(0, END)


def divide():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i = int(n1)
    e.delete(0, END)


def equals():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'subtraction':
        e.insert(0, i - int(n2))
    elif math == 'multiplication':
        e.insert(0, i * int(n2))
    else:
        e.insert(0, i / int(n2))

def clear():
    e.delete(0, END)


# button
button1 = Button(window, text='1', width=15, command=lambda: click(1))
button1.place(x=5, y=40)
button2 = Button(window, text='2', width=15, command=lambda: click(2))
button2.place(x=125, y=40)
button3 = Button(window, text='3', width=15, command=lambda: click(3))
button3.place(x=250, y=40)
buttonM = Button(window, text='x', width=15, command=multiply)
buttonM.place(x=375, y=40)
button4 = Button(window, text='4', width=15, command=lambda: click(4))
button4.place(x=5, y=80)
button5 = Button(window, text='5', width=15, command=lambda: click(5))
button5.place(x=125, y=80)
button6 = Button(window, text='6', width=15, command=lambda: click(6))
button6.place(x=250, y=80)
buttonP = Button(window, text='+', width=15, command=add)
buttonP.place(x=375, y=80)
button7 = Button(window, text='7', width=15, command=lambda: click(7))
button7.place(x=5, y=120)
button8 = Button(window, text='8', width=15, command=lambda: click(8))
button8.place(x=125, y=120)
button9 = Button(window, text='9', width=15, command=lambda: click(9))
button9.place(x=250, y=120)
buttonS = Button(window, text='-', width=15, command=subtract)
buttonS.place(x=375, y=120)
buttonC = Button(window, text='Clear', width=15, command=clear)
buttonC.place(x=5, y=160)
button0 = Button(window, text='0', width=15, command=lambda: click(0))
button0.place(x=125, y=160)
buttonE = Button(window, text='=', width=15, command=equals)
buttonE.place(x=250, y=160)
buttonD = Button(window, text='/', width=15, command=divide)
buttonD.place(x=375, y=160)

mainloop()

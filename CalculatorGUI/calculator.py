#!/usr/bin/python3

##################
# Imported modules
##################

from tkinter import *

###########
# Variables
########### 

numbers = []

###########
# Functions
###########

def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, "{}{}".format(current, number))

def buttonclear():
    e.delete(0, END)
    numbers.clear()

    if "labelFlag" in globals():
        equationLabel.destroy()

def buttonadd():
    numbers.append(e.get())
    numbers.append("+")
    e.delete(0, END)
    
def buttonsubstract():
    numbers.append(e.get())
    numbers.append("-")
    e.delete(0, END)
    
def buttonmultiply():
    numbers.append(e.get())
    numbers.append("*")
    e.delete(0, END)
    
def buttondivide():
    numbers.append(e.get())
    numbers.append("/")
    e.delete(0, END)
    
def buttonequals():
    if len(numbers) != 0:
        
        numbers.append(e.get())
        e.delete(0, END)

        equation = ""

        for i in numbers: 
            equation = equation + i + " "
        
        global equationLabel
        global labelFlag

        try:
            labelFlag
        except:
            labelFlag = None

        if labelFlag == True:

            equationLabel.destroy()

        equationLabel = Label(root, text = "Equation: {}".format(equation), justify = LEFT)
        equationLabel.grid(row = 2, column = 0, columnspan = 3)
        
        labelFlag = True
        total = 0
        
        while "*" in numbers:
            position = numbers.index("*")

            multiplication = float(numbers[int(position) - 1]) * float(numbers[int(position) + 1])
            numbers[position] = multiplication
            numbers.pop(position - 1)
            numbers.pop(position)

        while "/" in numbers:
            position = numbers.index("/")

            division = float(numbers[int(position) - 1]) / float(numbers[int(position) + 1])
            numbers[position] = division
            numbers.pop(position - 1)
            numbers.pop(position)

        flag = "+"
        
        for i in numbers:
            if i == "+":
                flag = "+"
            
            elif i == "-":
                flag = "-"

            elif flag == "+":
                total += float(i)
            
            elif flag == "-":
                total -= float(i)
        
        if total.is_integer() == True:
            e.insert(0, int(total))
        
        else:
            e.insert(0, total)

        numbers.clear()

##########################
# Graphical User Interface
##########################

root = Tk()
root.title("Calculator")

# Defining the display box

e = Entry(root)

# Putting the display box on the screen

e.grid(row = 1, column = 0, columnspan = 3, padx= 10, pady = 10)

# Defining the buttons

button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: buttonclick(0))
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: buttonclick(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: buttonclick(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: buttonclick(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: buttonclick(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: buttonclick(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: buttonclick(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: buttonclick(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: buttonclick(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: buttonclick(9))
buttoncomma = Button(root, text = ",", padx = 40, pady = 20, command = lambda: buttonclick("."))
buttonPlus = Button(root, text = "+", padx = 40, pady = 20, command = buttonadd)
buttonMinus = Button(root, text = "-", padx = 42, pady = 20, command = buttonsubstract)
buttonMultiply = Button(root, text = "*", padx = 40, pady = 20, command = buttonmultiply)
buttonDivide = Button(root, text = "/", padx = 41, pady = 20, command = buttondivide)
buttonEquals = Button(root, text = "=", padx = 40, pady = 20, command = lambda: buttonequals())
buttonClear = Button(root, text = "Clear", padx = 74, pady = 20, command = buttonclear)

# Putting the buttons on the screen

button0.grid(column = 0, row = 6)
buttonPlus.grid(column = 1, row = 6)
buttonMinus.grid(column = 2, row = 6)
buttonMultiply.grid(column = 0, row = 7)
buttonDivide.grid(column = 1, row = 7)
buttonEquals.grid(column = 2, row = 7)
buttoncomma.grid(column = 0, row = 8)
buttonClear.grid(column = 1, row = 8, columnspan = 2)


button1.grid(column = 0, row = 5)
button2.grid(column = 1, row = 5)
button3.grid(column = 2, row = 5)

button4.grid(column = 0, row = 4)
button5.grid(column = 1, row = 4)
button6.grid(column = 2, row = 4)

button7.grid(column = 0, row = 3)
button8.grid(column = 1, row = 3)
button9.grid(column = 2, row = 3)

# Looping over the tkinter logic

root.mainloop()
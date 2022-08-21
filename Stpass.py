import pyperclip
from tkinter import *
from random import *

#==========setting==========
root = Tk()
root.geometry('700x300')
root.resizable(width=FALSE, height=FALSE)
root.title('Stpass')
color = 'white'
root.configure('color')
#==========variables==========
basepassword = ''
password = 'dgjzyj'
#list
numbers = ['1','2','3','4','5','6','7','8','9',]
letters = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','*','~']
numbers_1 = 0
letters_2 = 0
symbols_3 = 0
a = 0
b = StringVar()

#==========frames==========
top_first = Frame(root, width=400, height=100, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=100, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=100, bg=color)
top_third.pack(side=TOP)
#==========functions==========
def generator() :
    global password
    password = ''
    for x in range(6) :
        a = randint(0 ,2)
        if a == 0 :
            numbers_1 = numbers[randint(0 ,8)]
            password = password + numbers_1[0]
        elif a == 1 :
            letters_1 = letters[randint(0 ,30)]
            password = password + letters_1[0]
        elif a == 2 :
            symbols_1 = symbols[randint(0 ,16)]
            password = password + symbols_1[0]
    b.set(password)
def copy() :
    pyperclip.copy(password)       
#==========screen==========
lbI_welcome = Label(root, text = 'welcome to strange password generator' , fg = 'black')
lbI_welcome.place(x = 240 , y = 20)

password_gr = Entry(root,bg='white' , textvariable = b)
password_gr.place(x = 160 , y = 90)

btn_run = Button(root, text = 'generate a password' , fg = 'black' ,command= generator)
btn_run.place(x = 160 , y = 50)

btn_copy = Button(root, text = 'copy password' , fg = 'black' , command = copy)
btn_copy.place(x = 160 , y = 130)

root.mainloop()

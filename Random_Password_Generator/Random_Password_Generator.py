import string
import random
from tkinter import *

root = Tk()
root.title('Random Password Generator')
root.geometry('600x400+0+0')


label_title = Label(root,text='Choose the strength of your password',fg='white',bg='blue',font=('times new roman',15))
label_title.pack()

label_space = Label(root)
label_space.pack()

def selection():
    selection = choice.get()

choice = IntVar()
rb1 = Radiobutton(root, text='Poor password',variable= choice, value=1, command=selection)
rb1.pack()
rb2 = Radiobutton(root, text='Avarage password',variable= choice, value=2, command=selection)
rb2.pack()
rb3 = Radiobutton(root, text='Advanced password',variable= choice, value=3, command=selection)
rb3.pack()

label_space = Label(root)
label_space.pack()
label_password = Label(root, text='Choose the strength of your password')
label_password.pack()

val = IntVar()
spinlength = Spinbox(root, from_=8 , to=30 , textvariable=val , width=15)
spinlength.pack()

def callback():
    result.config(text=passgen())

button_submit = Button(root,text='Generate Password',bg='green',fg='white',command=callback)
button_submit.pack(pady=20)

result = Message(root, text='',relief=RAISED, width=200, font=(25))
result.pack(pady=50)

poor = string.ascii_uppercase+string.ascii_lowercase
avarage = string.ascii_uppercase+string.ascii_lowercase+string.digits
advanced = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return"".join(random.sample(avarage, val.get()))
    elif choice.get()==3:
        return"".join(random.sample(advanced, val.get()))

root.mainloop()


 
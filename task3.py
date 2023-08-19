from tkinter import * 
 
import random
 
root = Tk()
root.geometry("400x300")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
name=StringVar()
 
 
def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)
 

 
 
Label(root, text="Password Generator", font="times-roman",fg='Blue').pack()
Label(root, text="Enter user name").pack(pady=0)
Entry(root,textvariable=name).pack()
Label(root, text="Enter password length").pack(pady=0)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password",bg='blue', command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Accept",fg='Blue').pack(pady=7)
Button(root, text="Reset",fg='Blue').pack(pady=8)

root.mainloop()
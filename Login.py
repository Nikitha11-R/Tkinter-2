from tkinter import *

window = Tk()
window.title("Login")
window.geometry("250x300")

frame = Frame(master = window, height= 200, width = 360, bg = "white")

lbl1 = Label(frame, text = "Full name", bg = "green", fg = "white", width = 12)
lbl2 = Label(frame, text = "Email Id", bg = "green", fg = "white", width = 12)
lbl3 = Label(frame, text = "Password", bg = "green", fg = 
"white", width = 12)

name = Entry(frame)
email = Entry(frame)
password = Entry(frame, show ="#")

def display():
    user = name.get()
    greet = "Hi!"+ user
    message = "\n Welcome to your account"
    txtbox.insert(END, greet)
    txtbox.insert(END, message)
txtbox = Text(bg = "white", fg = "black")

btn = Button(text = "Login", command = display, bg ="green")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name.place(x = 150, y = 20)
lbl2.place(x=20, y=80)
email.place(x=150, y= 80)
lbl3.place(x=20, y=140)
password.place(x = 150, y=140)
btn.place(x=130, y=210)
txtbox.place(y= 250)

window.mainloop()


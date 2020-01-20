from tkinter import *
master=Tk()

master.title("Hello World")
def print_text():
    print("Name: %s" % e1.get())
    
l1=Label(master, text="first name").grid(row=0)
b1=Button(master, text="Hello World! Click to close!??",command=print_text).grid(row=1,column =0)
e1=Entry(master)
e1.grid(row=0,column=1)
e1.insert(END,"Enter Your Name Here")
e1.delete(0,END)

mainloop()

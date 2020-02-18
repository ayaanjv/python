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
e=e1.get()
    e=int(e)
    e=e*9/5+32
    l3=Label(master, text=e).grid(row=0,column=3)

    
    
l1=Label(master, text="Celsius").grid(row=0)
l2=Label(master, text="Fahrenheit").grid(row=0,column=2)
b1=Button(master, text='Convert',command=print_text).grid(row=1,column =0)
e1=Entry(master)
e1.grid(row=0,column=1)
e1.insert(END,"Enter Your Name Here")
e1.delete(0,END)


mainloop()

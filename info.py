from tkinter import *
master=Tk()
def print_text():
   
    g1=e1.get()
    g2=e2.get()
    g3=e3.get()
    g4=e4.get()
    infobook=['first name:',g1,'last name:',g2,'address:',g3,'phone number:',g4]
    print (infobook)

master.title("Info Book")
b1=Button(master,text="Enter",command=print_text).grid(row=4,column =0)
l1=Label(master, text="first name").grid(row=0)
l2=Label(master, text="last name").grid(row=1)
l3=Label(master, text="address").grid(row=2)
l4=Label(master, text="phone number").grid(row=3)
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)



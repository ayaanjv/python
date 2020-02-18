import time
import random
from tkinter import *
master=Tk()

master.title("Hello World")


def print_text():

###CtoF
##    e=e1.get()
##    e=int(e)
##    e=e*9/5+32
##    l3=Label(master, text=e).grid(row=0,column=3)

###Calculator    
##    n=e1.get()
##    o=e2.get()
##    n2=e3.get()
##    n=int(n)
##    n2=int(n2)
##    if o=='+':
##        a=n+n2
##        l4=Label(master, text=str(a)).grid(row=0,column=5)
##    elif o=='-':
##        a=n-n2
##        l4=Label(master, text=str(a)).grid(row=0,column=5)
##    elif o=='*':
##        a=n*n2
##        l4=Label(master, text=str(a)).grid(row=0,column=5)
##    elif o=='/':
##        a=n/n2
##        l4=Label(master, text=str(a)).grid(row=0,column=5)
##    
    
###CT
##    e=e1.get()
##    e=str(e)
##    e= e.lower()
##    if e==coin:
##        l2=Label(master, text='correct').grid(row=2)
##    else :
##        l2=Label(master, text='wrong').grid(row=2)
    

###NBG
##    e=e1.get()
##    e=int(e)
##    if e==ran:
##        l2=Label(master, text='correct').grid(row=2)
##    elif e<ran:
##        l2=Label(master, text='bigger').grid(row=2)
##    elif e>ran:
##        l2=Label(master, text='smaller').grid(row=2)

### Timer
##    e=e1.get()
##    t=e
##    e=t
##    b1=Button(master, text="Reset",command=print_text).grid(row=1,column=1)
##
##    
##    for loop in range(int(e),-1,-1):
##        l2=Label(master, text=str(loop)+' ').grid(row=2)
##        time.sleep(1)
##        master.update()        
    
###First
##l1=Label(master, text="first name").grid(row=0)
##b1=Button(master, text="Hello World! Click to close!??",command=print_text).grid(row=1,column =0)
##e1=Entry(master)
##e1.grid(row=0,column=1)
##e1.insert(END,"Enter Your Name Here")
##e1.delete(0,END)

###Info
##l1=Label(master, text="Info").grid(row=0)
##b1=Button(master, text="Enter",command=print_text).grid(row=1,column =0)
##b2=Button(master, text="Quit",command=master.destroy).grid(row=2,column =0)
##e1=Entry(master)
##e1.grid(row=0,column=1)

###Timer
##l1=Label(master, text="Time").grid(row=0)
##b1=Button(master, text="Enter",command=print_text).grid(row=1,column=0)
##
##e1=Entry(master)
##e1.grid(row=0,column=1)

###NBG
##ran=random.randint(1,100)
##print(ran)
##l1=Label(master, text="Guess a number").grid(row=0)
##b1=Button(master, text="Enter",command=print_text).grid(row=1,column=0)
##e1=Entry(master)
##e1.grid(row=0,column=1)

###CT
##coin=''
##flip=random.randint(1,2)
##if flip==1:
##    coin='tails'
##else:
##    coin='heads'
##l1=Label(master, text="Heads or Tails").grid(row=0)
##b1=Button(master, text="Enter",command=print_text).grid(row=1,column=0)
##e1=Entry(master)
##e1.grid(row=0,column=1)

###Calculator
##a=0
##b1=Button(master, text="Enter",command=print_text).grid(row=0,column=4)
##e1=Entry(master)
##e2=Entry(master)
##e3=Entry(master)
##e1.grid(row=0,column=1)
##e2.grid(row=0,column=2)
##e3.grid(row=0,column=3)
##l1=Label(master, text="Number").grid(row=1,column=1)
##l2=Label(master, text="Operator").grid(row=1,column=2)
##l3=Label(master, text="Number").grid(row=1,column=3)

###CtoF
##l1=Label(master, text="Celsius").grid(row=0)
##l2=Label(master, text="= Fahrenheit").grid(row=0,column=2)
##b1=Button(master, text='Convert',command=print_text).grid(row=1,column =0)
##e1=Entry(master)
##e1.grid(row=0,column=1)
##e1.insert(END,"Enter Your Name Here")
##e1.delete(0,END)


mainloop()

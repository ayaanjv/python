from tkinter import*
from tkinter import scrolledtext
import socket
import threading

host='192.168.0.14'  # server side ip address
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

def sendMessage():
    e=You.get()
    You.delete(0,END)
    chatBox.insert(INSERT,e+"\n")
    s.send(e.encode())
def recieveMessage():
    global conn
    while 1:
      data=s.recv(1024).decode('utf-8')
      chatBox.insert(INSERT,data+"\n")
    s.close()

rThread=threading.Thread(target=recieveMessage)
rThread.start()

root=Tk()
root.title('Client')
root.geometry('300x300')
root.configure(bg='light cyan')

chatBox=scrolledtext.ScrolledText(root,highlightbackground = 'light cyan',
                                  highlightcolor= 'light cyan',
                                  wrap = WORD,  
                                  width = 40,  
                                  height = 10,  
                                  font = ("Times New Roman",  15)) 
You=Entry(root, bg='light cyan',
            highlightbackground = 'light cyan',
            highlightcolor= 'light cyan')

Send=Button(root,text='Send', command=sendMessage, bg='light cyan',
            highlightbackground = 'light cyan',
            highlightcolor= 'light cyan')

chatBox.pack()
You.pack()
Send.pack()

root.mainloop()

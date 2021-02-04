from tkinter import*
from tkinter import scrolledtext
from tkmacosx import Button
import socket
import threading

host='192.168.0.14'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind((host, port))
print('socket binded to', port)
backlog=5
s.listen(backlog)
conn,addr = s.accept()

def sendMessage():
    e=You.get()
    You.delete(0,END)
    chatBox.insert(INSERT,e+"\n")
    conn.send(e.encode())
  
def recieveMessage():
    while 1:
      data=conn.recv(1024).decode('utf-8')
      chatBox.insert(INSERT,data+"\n")
    conn.close()
    
rThread=threading.Thread(target=recieveMessage)
rThread.start()

root=Tk()
root.title('Sever')
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

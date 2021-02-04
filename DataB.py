import sqlite3
conn=sqlite3.connect('test.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT)') 




username={}
print('Do you want to sign in or sign up?(i/u)')
sign=input()

if sign=='u':
    print('what will your username be')
    user=input()
    print('what will your password be')
    password=input()
    c.execute('SELECT * FROM accounts WHERE username= ?',(user,))
    fetch=c.fetchall()
    if len(fetch)==0:
        c.execute('INSERT INTO accounts VALUES(?,?)',(user, password))
    else:
        print('This account already exists')
if sign=='i':
    print ('what is your username')
    user=input()
    c.execute('SELECT*FROM accounts WHERE username=?',(user,))
    fetch=c.fetchone()
    
    if fetch is not None and fetch[0]==user:
        print ('what is your password')
        password=input()
        if fetch[1]==password:
            print('Login succesful')
        else:
            print('password is incorrect')
    else:
        print("this account doesn't exist")
conn.commit()
c.close()
conn.close()    

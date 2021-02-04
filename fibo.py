import time

##a=0
##b=1
##c=None
##fiboNum=[]
##fiboNum.append(a)
##fiboNum.append(b)
##
##def fibo (num):
##    global a
##    global b
##    global c
##
##    c=a+b
##    fiboNum.append(c)
##    a=b
##    b=c
##    
##    
##    if len(fiboNum)==num:
##        print(fiboNum)
##    else:
##        fibo(n)
##        
##n=int(input('how long should the sequince be '))
##fibo(n)

##print("Give me a number to find it's it factorial")
##fact=int(input())
##count=fact
##def calculate():
##    global count
##    global fact
##    
##    count=count-1
##    fact=fact*count
##    print(fact)
##    if count>2:
##        calculate()
##calculate()

a=0
b=1
layer=[1,1]
copyList=[]
print ('how long do you want the triangle to be')
n=int(input())

print(layer)
def recurse(num):
    global a
    global b
    global copyList
    global layer
    global n

    for adding in range(len(layer)-1):
        a=layer[adding]
        
        b=layer[adding+1]
        addParts=a+b
        copyList.append(addParts)
    
        
      
    layer=[]   
    layer=[1]+copyList+[1]    
    copyList=[]
    n=n-1
    print(layer)
    if n>=1:
        recurse(n-1)
        
    

recurse(n)
    
    
    
        
    

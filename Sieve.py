num=[2,3,4,5,6,7,8,9,10]
nextNum=0
def prime():
    global nextNum
    p=num[nextNum]

    if p*p in num:
        for step in num:
            if step % p==0 and step!=p:
                num.remove(step)


    else:
        print(num)
    
   
    print(num)
    
    nextNum=nextNum+1
    if num[nextNum]<10**0.5:
        prime()


prime()
    
                
        

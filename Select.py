import random ###Selection Sort
ranNum=[]
for loop in range(1,11,1):
    ran=random.randint(1,100)
    ranNum.append(ran)
a=0
b=0
count=0
nextNum=0
value=0
restart=0
check={}
print(ranNum)



def sort():
    global count
    global nextNum
    global check
    global value
    
    a=ranNum[count]
    b=ranNum[nextNum]

       

    if b<a :
        if len(check)==0:
            value=b
            check[value]=nextNum
        else:
            if b< ranNum[check[value]]:
                value=b
                check={}
                check[value]=nextNum
        
    

    if nextNum<len(ranNum)-1 :
        nextNum=nextNum+1
    else:
        if len(check)!=0:
            ranNum[count],ranNum[check[value]]=ranNum[check[value]],ranNum[count]   
        count=count+1
        nextNum=count
        
        check={}
        print(ranNum)

    if count<len(ranNum)-1:
        sort()
sort()

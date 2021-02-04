import random
ranNum=[]
for loop in range(1,11,1):
    ran=random.randint(-100,100)
    ranNum.append(ran)

a=0
b=1S
count=0
nextNum=1
stop=1
a=ranNum[count]
b=ranNum[nextNum]
check=0
while True:
    
    a=ranNum[count]
    b=ranNum[nextNum]
    
    if a>b:
        ranNum[count],ranNum[nextNum]=ranNum[nextNum],ranNum[count]
        count=nextNum
        nextNum=nextNum+1
        
    elif a<b:
        count=nextNum
        nextNum=nextNum+1
       
        
    if nextNum==len(ranNum):
        count=0
        nextNum=1







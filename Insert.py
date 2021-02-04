import random

##ranNum=[5, 8, 3, 5, 9, 6, 10, 2, 4, 7]
ranNum=[]
for loop in range(1,11,1):
    ran=random.randint(1,100)
    ranNum.append(ran)
sortNum=0
count=1
countOff=0
a=ranNum[count]
b=ranNum[countOff]



def sort():
    
    a=ranNum[count]
    b=ranNum[countOff]


    print(ranNum)
    
    if a<=b:
         countOff=countOff-1

         
    if a>b and countOff!=count-1:        
        ranNum.insert(countOff+1,a)
        ranNum.pop(count+1)
        countOff=count
        count=count+1
    elif a>b and countOff==count-1:
        countOff=count
        count=count+1
    
 
    
    if countOff==0:        
##        if a>ranNum[0]:
##            ranNum.insert(1,a)
##            ranNum.pop(count+1)
##            countOff=count
##            count=count+1
           
        if a<ranNum[0]:
            ranNum.insert(countOff,a)
            ranNum.pop(count+1)
            countOff=count
            count=count+1

        
    if count==len(ranNum):
        print(ranNum)
        
    else:
        sort()
sort()
    


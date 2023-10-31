#number series
i=k=l=y=1
while i<9:
    y=1
    while y<9:
        if y<=9-i:
            print('',end=' ')
            y+=1
        else:
            break 
    k=1  
    while k<9:
        if k<i-1:
            print(k,end=' ')
            k+=1
        else:
            break
    l=1
    while l<9:
         j=i-l
         if j>0:
            print(j,end=' ')
            l+=1
         else:
            print(" ")
            break
    i+=1

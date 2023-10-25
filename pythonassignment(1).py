#minimum of nos with func
l=[]
for i in range(5):
    n=int(input("Enter number: "))
    l.append(n)
print("Minimum number is",min(l))

#minimum of nos without func
l1=[]
l2=[]
for j in range(5):
    n1=int(input("Enter number: "))
    l1.append(n1)
k=l1[0]
for i in l1:
    if  i<k:
        k=i
        l2.append(k)
print("Minimum number is: ",l2)

#armstrong number
x=int(input("enter the number: "))
z=x
l=[]
while x>0:
    y=x%10
    l.append(y)
    x=x//10   
print(l)
c=0
for i in l:
    c+=i**3
print(c)
if c==z:
    print(z, " is an armstrong number")
else:
    print(z, "is not an armstrong number")

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

x=float(input("enter angle in radians: "))
sign=-1
t=int(input("Enter number of terms for calculation: "))
s=1
for i in range(2,t+1):
    n=(2*i)-2
    num=(sign*i)*(x**n)
    den=fact(n)
    s+=num/den
print("values of cos",x,"is",s)

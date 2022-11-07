def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter frst number:"))
b=int(input("enter second number:"))
print("gcd of",a,"and",b,"is:")
print(gcd(a,b))

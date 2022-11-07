a=input("enter the word:")
l1=[]
for i in range(len(a)):
    l1.append(a[i])
l2=[l1[0]]
for i in range(1,len(a)):
    if(l1[i]==l1[0]):
        l2.append("$")
    else:
        l2.append(l1[i])

print(l2)
               

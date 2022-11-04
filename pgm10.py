l1=[]
l2=[]
n=int(input("enter the length of list:"))
for i in range(n):
    l1.append(int(input("enter the numbers in the list:")))
l1=list(map(int,l1))
print(l1)
for j in range(n):
    if l1[j]<100:
        l2.append(l1[j])
    else:
        l2.append("over")
print(l2)

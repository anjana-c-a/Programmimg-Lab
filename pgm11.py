l1=input("enter names:").split()
print(l1)
count=0
for i in l1:
    for j in i:
        if(j=='a'):
            count=count+1
print("count(a):",count)

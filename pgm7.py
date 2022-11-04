a=[]
a=input("Enter the elements of list1: ")
a=a.split(" ") 
a=list(map(int,a))
print(a)
b=[]
b=input("Enter the elements of list2: ")
b=b.split(" ") 
b=list(map(int,b))
print(b)
len1=len(a)
len2=len(b)
print("Length of fist list: ",len1)
print("length of second list: ",len2)
if(len1==len2):
    print("Lists are of same length")
else:
    print("Lists are of different length")
total=0
for i in range(0,len1):
    total=total+a[i]
print("Sum of first list is:",total)
total2=0
for i in range(0,len2):
    total2=total2+b[i]
print("Sum of second list is:",total2)
if total==total2:
	print("Sum of lists are same")
else:
	print("Sum of lists are not same")
for i in range(0,len1):
	for j in range(0,len2):
		if a[i]==b[j]:
				print(a[i])
				print("Occurs in both lists")


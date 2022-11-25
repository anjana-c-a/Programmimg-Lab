def total(l1):
	tot=0
	for i in l1:
		tot=tot+i
	print("total sum:",tot)
l1=[]
n=int(input("Enter the no of elements:"))
for i in range(0,n):
	el=int(input("Enter the element:"))
	l1.append(el)
print(l1)
total(l1)

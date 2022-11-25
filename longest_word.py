def long(l1):
	a=[]
	for i in l1:
	 b=len(i)
	 a.append(b)
	a.sort()
	print("The length of longest word is",a[-1])
	

l1=[]
el=input("Enter the words:")
l1=el.split(" ")
print(l1)
long(l1)

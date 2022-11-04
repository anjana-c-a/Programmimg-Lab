a=[]
a=input("Enter the elements of list1: ")
a=a.split(" ") 
a=list(map(int,a))
print(a)
b=[x for x in a if x%2!=0]
print("The  list of numbers removing even numbers:")
print(b)

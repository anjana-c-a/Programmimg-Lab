a=[]
a=input("Enter the elements of list1: ")
a=a.split(" ") 
a=list(map(int,a))
print(a)
b=[x for x in a if x>0]
print("The positive list of numbers are:")
print(b)
print("The square of elements of given list is:")
c=[x*x for x in a]
print(c)
word=input("enter the word:")
print(word)
vowels=["a","e","i","o","u"]
d=[x for x in word if x in vowels]
print("vowels is",d)
c=[ord(x) for x in word]
print("The ordinal value is:",c)




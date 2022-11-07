a=[]
word=input("Enter a sentence:")
st1=input("Enter a Word:")
a=word.split(" ")
count=0
for i in a:
    if i==st1:
        count=count+1
print(count)

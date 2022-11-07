dict1={}
n=int(input("number of items in a dictionary 1:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
print(dict1)
dict2={}
m=int(input("enter number of items in dectionary 2:"))
for i in range(m):
    key=input("enter key:")
    value=input("enter value:")
    dict2[key]=value
print(dict2)
dict3={**dict1,**dict2}
for k,v in dict3.items():
    if k in dict1 and k in dict2:
        dict3[k]=[v,dict1[k]]
print(dict3)
        

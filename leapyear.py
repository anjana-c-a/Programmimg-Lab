year=int(input("Enter a future year:"))
for i in range(2022,year):
 if (i % 400 == 0) and (i % 100 != 0) or (i % 4 ==0):
 	print(i)


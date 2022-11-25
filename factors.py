def factors(n):
	for i in range (1,n+1):
		if n%i==0:
			print("The factors of the given number is:",i)
n=int(input("Enter a number:"))
factors(n)
		


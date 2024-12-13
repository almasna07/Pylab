n=int(input("Enter the Number of Terms:"))
fibonacci=[0,1]
for i in range(2,n):
	next=fibonacci[i-1]+fibonacci[i-2]
	fibonacci.append(next)
print("Fibonacci Series is:",fibonacci[:n])

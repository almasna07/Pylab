def fact(x):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact
n=int(input("Enter The Number of Terms:"))
terms=list(map(lambda x:(x**x)/fact(x),range(1,n+1)))
sum=0
for s in terms:
	sum+=s
print(f"Sum of Terms:{sum}")

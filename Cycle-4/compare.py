def compare(s1,s2,n):
	if n<=0:
		raise ValueError("Number must be positive!!")
	return s1[:n]==s2[:n]
string1=input("Enter the First String:")
string2=input("Enter the Second String:")
n=int(input("Enter the Number of Characters:"))
print(f"Equivalnce={compare(string1,string2,n)}")

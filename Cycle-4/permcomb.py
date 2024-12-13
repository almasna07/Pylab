import math
def permutation(n,r):
	return math.factorial(n)//math.factorial(n-r)
def combination(n,r):
        return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
n=int(input("Enter The Value for n:"))
r=int(input("Enter The Value for r:"))
print(f"Permutation:{permutation(n,r)}")
print(f"Combination:{combination(n,r)}")



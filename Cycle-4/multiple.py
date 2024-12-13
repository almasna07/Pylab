n=list(map(int,input("Enter The Number Seperated By spaces:").split()))
mul=list(filter(lambda x:x%3 == 0,n))
print(f"Multiples of 3:{mul}")

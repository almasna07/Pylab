numbers=[int(x) for x in input("Enter numbers seperated by space: ").split()]
total_sum=0
for num in numbers:
	total_sum+=num
print("sum of all items:",total_sum)

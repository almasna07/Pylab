number=input("Enter integers seperated by commas : ").split(',')
result=[] #Empty list
for  num in number:
	number=int(num)
	if number%2!=0:
        	result.append(number)
print(result)

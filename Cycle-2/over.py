number=input("Enter integers seperated by commas : ").split(',')
result=[] #Empty list
for  num in number:
	if int(num)>100:
		result.append('over')
	else:
		result.append(int(num))
print(result)

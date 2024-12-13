str=input("Enter a string : ")
if len(str)>=3 and str[-3:]=="ing":
	str+="ly"
else:
	str+="ing"
print("String is:",str)

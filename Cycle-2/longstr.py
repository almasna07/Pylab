words=input("Enter the words seperated by commas : ").split(',')
length=0
for word in words:
	if len(word)>length:
		length=len(word)
print("Length of the longest word is:",length)

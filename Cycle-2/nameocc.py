names=input("Enter first names seperated by commas : ")
count=sum(name.lower().count('a') for name in names)
print("Occurences of 'a':",count)

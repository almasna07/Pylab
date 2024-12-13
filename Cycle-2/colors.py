list1=input("Enter colors of list1 seperated by commas : ")
list2=input("Enter colors of list2 seperated by commas : ")
set1=set(list1.split(','))
set2=set(list2.split(','))
diff=set1-set2
print("Difference of set1 and set2 is:",diff)

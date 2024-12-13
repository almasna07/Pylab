list1=input("Enter first list of integers : ")
list1=[int(num) for num in list1]
list2=input("Enter first list of integers : ")
list2=[int(num) for num in list2]
print("Same Length:",len(list1)==len(list2))
print("Sum to same value:",sum(list1)==sum(list2))
print("Value occur on both:",bool(set(list1)==set(list2)))


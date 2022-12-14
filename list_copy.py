#thislist = ["apple", "banana", "cherry"]
#mylist = thislist.copy()
#print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
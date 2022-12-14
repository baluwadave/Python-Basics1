new_list = [x for x in range (10) if x<5]
print(new_list)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
thislist = ["Orange", "Mango", "kiwi", "Pineapple", "banana","apple"]
#thislist.sort(reverse = True)

#thislist.sort()

thislist.sort(key=str.lower)
print(thislist)
list = [100,50,6,5,65,82,23,55]
list.sort(reverse = True)

#ist.sort()

print(list)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)

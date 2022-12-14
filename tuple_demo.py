tuple=("apple","banana","cherry")
#print (tuple)
#print("tuple allows duplicate values:")
tuple1=("apple","banana","cherry","apple","banana","cherry")
#print (tuple1)
#print("find the length of tuple1.")
#print(len(tuple1))
#print ("create a tuple with one item")
tuple2 = ("apple",)
#print(type(tuple2))
#NOT a tuple
thistuple = ("apple")
#print(type(thistuple))
#Tuple items can be of any data type:
tuple3 = ("abc", 34, True, 40, "male")
#print(type(tuple3))
thistuple1= ("apple", "banana", "cherry") # note the double round-brackets
#print(thistuple1)

thistuple = ("apple", "banana", "cherry")
#print(thistuple[1])

# print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,
print(thistuple[-4:-1])



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")





# Create a Set:


set1 ={"apple","mango","cherry","banana"}
print(set1)


# Duplicate values will be ignored:

set_1 = {"apple", "banana", "cherry", "apple"}

print(set_1)


# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False}

print(set1)
print(set2)
print(set3)


# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)



# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))



# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print(type(thisset))
#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)





# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("mango" in thisset)




#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)




# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("cherry")

print(thisset)

# Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

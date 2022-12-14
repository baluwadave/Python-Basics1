#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

#print(green)
#print(yellow)
#print(red)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)






# Iterate through the items and print the values:
#thistuple = ("apple", "banana", "cherry")
#for x in thistuple:
#  pass

  #print(x)
# Print all items by referring to their index number:
 #thistuple = ("apple", "banana", "cherry")
  #for i in range(len(thistuple)):
      #pass

     # print(thistuple[i])

     # Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
        print(thistuple[i])
        i = i + 1



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


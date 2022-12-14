# In Python a function is defined using the def keyword:


def my_function():
    print("Hello from a function")

#To call a function, use the function name followed by parenthesis:
my_function()



#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")






#This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")




#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")






#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")







#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Wadave")



#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a list as an arguments



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



#Returns Values
def my_function(x) :
    for x in  range (11):
       z= x * 5
    print(z)





    my_function(x)
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))







#Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
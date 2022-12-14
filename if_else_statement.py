
#In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a.
# As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

a = 33
b = 200
if b > a:
    pass
 #   print("b is greater than a")


#If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
    pass
#print("b is greater than a") # you will get an error


#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("********************************************************")
#The else keyword catches anything which isn't caught by the preceding conditions.


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("********************************************************")





#You can also have an else without the elif:


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print("********************************************************")


#One line if statement:

if a > b: print("a is greater than b")


print("********************************************************")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

print("********************************************************")


#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print("********************************************************")

#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a < c:
  print("At least one of the conditions is True")


#You can have if statements inside if statements, this is called nested if statements.


x = 11

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
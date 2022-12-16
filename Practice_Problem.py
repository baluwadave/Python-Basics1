#create a list
exp = [2200,2350,2600,2130,2190]
print("In Feb, how many dollars you spent extra compare to January? ",exp[1]-exp[0])
# Find out your total expense in first quarter (first three months) of the year.
print("  your total expense in first quarter (first three months) of the year.",exp[:3])
#Find out if you spent exactly 2000 dollars in any month
if 2000 in exp:
    print ("I  have spent greater than 2000$ ")
else:

    print("i have not spent exact 2000$" )

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

exp.append(1980)
print(exp)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


exp[3]=exp[3]-200
print ("updated april month expences :",exp[3])







heros=['spider man','thor','hulk','iron man','captain america']
#Length of the list

print(len(heros))
#Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)


# You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3,'balck panther')
print(heros)



#  Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros[1:3]=['doctor strange']
print(heros)


# 5. Sort the list in alphabetical order
heros.sort()
print(heros)



#Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function



max = int (input("Enter the max number :"))
odd_nmbers=[]
for i in range(1,max):
    if i%2 == 1 :
        odd_nmbers.append(i)
print("odd numbers",odd_nmbers)






def swaplist(newlist):
    size =  len(newlist)
    #swapping
    temp = newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
#driver code
newlist = [12,35,9,56,24]
print(swaplist(newlist))


print("***************************************")

def swaplist(list):

    list[0],list[-1]=list[-1],list[0]
    return (list)
list =[12,35,9,56,24]
print(swaplist(list))



print("****************************************")
def swaplist(list):
    get = list[0],list[-1]
    list[-1],list[0] = get
    return list
list_1 = [12,254,4,5,85,44]
print(swaplist(list_1))



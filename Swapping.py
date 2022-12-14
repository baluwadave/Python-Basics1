#swap the elements in the list from pos 2 to pos 1


def swapping (list,pos1,pos2):
    list[pos1],list [pos2] = list[pos2],list[pos1]
    return list
list = [25,55,6,79,85]
pos1, pos2=0,3
print(swapping(list,pos1, pos2))
def LinearSearch(list,item,start=0,end=None):
    if end == None or start>end:
        return -1

    for i in range(start,end):
        if list[i]==item:
            return i
    return -1

l = [i for i in range(0,100)]
print(LinearSearch(l,33,0,len(l)))
print(LinearSearch(l,100,0,len(l)))
print(LinearSearch(l,0,0,len(l)))
print(LinearSearch(l,99,0,len(l)))
print(LinearSearch(l,-1,0,len(l)))

def BinarySearch(list,item,start = 0, end = None):
    if end==None or start>end:
        return -1
    end-=1
    while start<=end:
        mid = (start + end)//2
        if list[mid]==item:
            return mid

        elif list[mid]>item:
            end = mid-1

        else:
            start = mid+1
    return -1


l = [i for i in range(0,100)]
print(BinarySearch(l,33,0,len(l)))
print(BinarySearch(l,100,0,len(l)))
print(BinarySearch(l,0,0,len(l)))
print(BinarySearch(l,99,0,len(l)))
print(BinarySearch(l,-1,0,len(l)))




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

def ExponentialSearch(list,item,start = 0,end = None):
    if start>end or end==None:
        return -1
    if list[start]==item:
        return start
    i=1
    while(start+i<end and item>list[start+i]):
        i*=2

    if start+i<=end and list[start+i]==item:
        return start+i
    return BinarySearch(list,item,start=start+i//2,end=min(start+i,end))


l = [i for i in range(0,100)]
print(ExponentialSearch(l,33,0,len(l)))
print(ExponentialSearch(l,100,0,len(l)))
print(ExponentialSearch(l,0,0,len(l)))
print(ExponentialSearch(l,99,10,len(l)))
print(ExponentialSearch(l,-1,0,len(l)))




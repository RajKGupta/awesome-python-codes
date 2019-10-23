def swap(l,i,j):
    temp = l[i]
    l[i]=l[j]
    l[j]=temp

def partition(l,low,end):
    pivot = l[end]
    pos = low-1
    for j in range(low,end):
        if l[j]<pivot:
            pos+=1
            swap(l,pos,j)
    swap(l,pos+1,end)
    print(l)
    return pos+1

def QuickSort(l,low,end):
    if low<end:
        p = partition(l,low,end)
        QuickSort(l,low,p-1)
        QuickSort(l,p+1,end)


l = [i for i in range(10,0,-1)]
QuickSort(l,0,len(l)-1)
print(l)


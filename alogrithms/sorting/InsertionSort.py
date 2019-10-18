def InsertionSort(l,len):
    for i in range(1,len):
        temp = l[i]
        for j in range(i-1,-1,-1):
            if temp<l[j]:
                l[j+1]=l[j]
            else:
                break
        l[j]=temp

l = [i for i in range(10,1,-1)]
InsertionSort(l,len(l))
print(l)


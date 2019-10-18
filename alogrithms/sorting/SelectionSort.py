def SelectionSort(l,len):
    for i in range(0,len-1):
        min = l[i]
        pos = i

        for j in range(i+1,len):
            if min>l[j]:
                min = l[j]
                pos = j
        l[pos] = l[i]
        l[i] = min

l = [i for i in range(100,1,-1)]
SelectionSort(l,len(l))
print(l)


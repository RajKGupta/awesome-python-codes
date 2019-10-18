def BubbleSort(l,len):
    for i in range(len):
        for j in range(1,len-i):
            if l[j-1]>l[j]:
                temp = l[j-1]
                l[j-1]=l[j]
                l[j] = temp
l = [i for i in range(10,1,-1)]
BubbleSort(l,len(l))
print(l)


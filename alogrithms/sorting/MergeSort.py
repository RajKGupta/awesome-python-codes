def MergeSort(l,len):
    if len>1:
        mid = len//2
        L = l[:mid]
        R = l[mid:]
        L = MergeSort(L,mid)
        R = MergeSort(R,len-mid)

        i,j,k=0,0,0
        f = [None]*len
        while(i<mid and j<len-mid):
            if L[i]<R[j]:
                f[k]=L[i]
                k+=1
                i+=1
            else:
                f[k]=R[j]
                k+=1
                j+=1

        while i<mid:
            f[k]=L[i]
            k+=1
            i+=1

        while j<len-mid:
            f[k]=R[j]
            k+=1
            j+=1
        return f
    else:
        return l

l = [i for i in range(10,1,-1)]
print(MergeSort(l,len(l)))
print(l)


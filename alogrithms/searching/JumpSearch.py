"""
The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or
skipping some elements in place of searching all elements.

What is the optimal block size to be skipped?
In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to
 be searched for, we perform m-1 comparisons more for linear search. Therefore the total number of
 comparisons in the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will
  be minimum when m = √n. Therefore, the best step size is m = √n.
"""
import math
def JumpSearch(ar,item,start = 0, end = None):
    if end == None or start>end:
        return -1
    n = end - start + 1
    m = int(math.sqrt(n))
    pos = None
    i = start
    while(i<end):
        if ar[i]==item:
            return i
        elif ar[i]>item:
            pos = i
            break
        elif i==end-1:
            return -1

        i=min(end-1,i+m)

    for i in range(pos-m,pos):
        if ar[i]==item:
            return i

    return -1

l = [i for i in range(0,100)]
print(JumpSearch(l,33,0,len(l)))
print(JumpSearch(l,100,0,len(l)))
print(JumpSearch(l,0,0,len(l)))
print(JumpSearch(l,99,0,len(l)))
print(JumpSearch(l,-1,0,len(l)))




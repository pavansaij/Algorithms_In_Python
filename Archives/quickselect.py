def partition(i,j):    
    pivot = arr[i]
    lo = i+1
    hi = j
    while (hi > lo):
        while (arr[lo] <= pivot):
            if lo == j:
                break
            lo+=1
            
        while (arr[hi] > pivot):
            if hi == i:
                break
            hi-=1
        if (lo >= hi):
            break
        arr[lo],arr[hi] = arr[hi],arr[lo]
    arr[i],arr[hi] = arr[hi],arr[i]
    return hi

def quickselect(k,st,en):
    if (en-st) == 1 or (en-st) == 0:
        if arr[st] > arr[en]:
            arr[en],arr[st] = arr[st],arr[en]
        return arr[k]
    elif (st < en):
        piv = partition(st,en)
        if piv == k:
            return arr[k]
        elif piv < k:
            return quickselect(k,piv+1,en)
        elif piv > k:
            return quickselect(k,st,piv-1)

arr = list(map(int, input().split(" ")))
k = int(input())
print(quickselect(k,0,len(arr)-1))
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

def quicksort(st,en):
    if (en-st) == 1:
        if arr[st] > arr[en]:
            arr[en],arr[st] = arr[st],arr[en]
    elif (st < en):    
        piv = partition(st,en)
        quicksort(st,piv-1)
        quicksort(piv+1,en)

arr = [-2,1,5,8,-9,-121311]
quicksort(0,len(arr)-1)
print(arr)
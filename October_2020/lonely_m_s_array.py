#https://www.hackerearth.com/challenges/competitive/october-circuits-20/algorithm/the-alones-array-459a5370

n = int(input())
lis = list(map(int, input().split()))

def asc_sorted_pattern(arr, st ,en):
    prev = float('-inf')

    for i in range(st, en):
        if prev < arr[i]:
            prev = arr[i]
            continue
        return i
    
    return float('inf')

def desc_sorted_pattern(arr, st, en):
    prev = float('inf')

    for i in range(st, en):
        if prev > arr[i]:
            prev = arr[i]
            continue
        return i
    
    return float('inf')

cur, asc, res = 0, True, 0

while cur < n:
    if asc:
        cur = asc_sorted_pattern(lis, cur, n)
    else:
        cur = desc_sorted_pattern(lis, cur, n)
    
    asc = not asc
    res += 1

print(res)

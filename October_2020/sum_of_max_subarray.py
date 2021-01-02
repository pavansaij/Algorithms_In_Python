def nge(arr, n):
    res = [1 for _ in range(n)]
    s = []

    for i in range(n-1, -1 , -1):
        while (len(s) > 0 and arr[s[-1]] <= arr[i]):
            s.pop()
        
        if len(s) > 0:
            x = abs(i-s[-1])
            if x > 0:
                res[i] = (x*(x+1))//2
        else:
            x = abs(i-n)
            if x > 0:
                res[i] = (x*(x+1))//2

        s.append(i)
    return res

n,q = map(int, input().split())
arr = list(map(int, input().split()))

fwd = nge(arr, n)
bck = nge(arr[::-1], n)[::-1]

print(fwd)
print(bck)

total = [fwd[i]+bck[i]-1 for i in range(n)]
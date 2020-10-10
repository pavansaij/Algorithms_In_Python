
# Write your code here

def fill(cnt, up_hill, till):
    res = ""
    if up_hill:
        for i in range(till+count,till-1,-1):
            res += chr(i+ord('a'))
    else:
        for i in range(till,till+count+1,1):
            res += chr(i+ord('a'))
    
    return res

t = int(input())
for _ in range(t):
    s = input()
    res, prev, up_hill, count, till = "", None, None, 0, 0
    for c in s:
        if prev:
            if prev != c:
                res += fill(count, up_hill, till)
                till = ord(res[0])-ord('a') if up_hill else ord(res[-1])-ord('a')
                count = 0 

            up_hill = c == ">"
            count += 1
        else:
            up_hill = c == ">"
            count += 1
        prev = c1
    
    if count > 0:
        res += fill(count, up_hill, till)
    print(res)


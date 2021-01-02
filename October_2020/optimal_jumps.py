'''
Question - https://media.discordapp.net/attachments/750701231961538581/764507217465442404/optimum_jump1.png?width=1064&height=665

import time
import sys
import random

def move(current, dist):
    dest = (current + dist)
    return dest >= 0 and (dest not in memo)

def solve_util(current, cummilative):
    global arr
    global memo

    if current >= len(arr):
        return cummilative,0

    if current not in memo:
        memo[current] = float('inf')

    cummilative += arr[current]

    res_bck, res_fwd = [float('inf'), 0], [float('inf'), 0]

    if move(current, -1):
        res_bck = solve_util(current-1, cummilative)
    elif current-1 in memo and memo[current-1] != float('inf'):
        memo[current] = min(memo[current], memo[current-1] + arr[current])
        return memo[current-1] + cummilative, memo[current-1]

    if move(current, 2):
        res_fwd = solve_util(current+2, cummilative)
    elif current+2 in memo and memo[current+2] != float('inf'):
        memo[current] = min(memo[current], memo[current+2] + arr[current])
        return memo[current+2] + cummilative, memo[current+2]
    
    memo[current] = min([memo[current], res_fwd[1]+arr[current], res_bck[1]+arr[current]])

    return min(res_bck[0], res_fwd[0]), arr[current]

oldlimit = sys.getrecursionlimit()
arr = []
memo = {}


n = 9000

sys.setrecursionlimit(100000)
for _ in range(n):
    arr.append(random. randint(1,1000))

in_t = time.time()
print(solve_util(0,0)[0])
out = time.time()
print(out - in_t)

sys.setrecursionlimit(oldlimit)

'''

n = int(input())
times = [(None, None) for _ in range(n)]

def cond(tup1, tup2):
    return max(tup1[0], tup2[0]) >= min(tup1[1], tup2[1])

for i in range(n):
    times[i][0] = int(input())

for i in range(n):
    times[i][1] = int(input())

times = sorted(times, key=lambda x: (x[0], x[1]))

max_intersec, temp = 0, 0
for i in range(1,n):
    if not cond(times[i-1], times[i]):
        temp += 1
    else:
        max_intersec = max(max_intersec, temp)
        temp = 0

max_intersec = max(temp, max_intersec)

print(1 if max_intersec<=2 else 0)
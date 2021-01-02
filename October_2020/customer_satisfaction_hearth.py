import math

def is_possible(t, e, mp):
    cur = t
    for i in range(1, e+1):
        if i in mp and mp[i] > cur:
            return False
        else:
            cur = cur - mp.get(i, 0)
        
        cur += t
    return True

def binary(st, en, mp, end_max):
    tar = (st + en)//2

    is_tar_pos = is_possible(tar, end_max, mp)

    if is_tar_pos and (not(is_possible(tar-1, end_max, mp)) or st == en):
        return tar

    if is_tar_pos:
        return binary(st, tar, mp, end_max)
    else:
        return binary(tar, en, mp, end_max)

t = int(input())
for _ in range(t):
    n = int(input())
    mp, end_max = {}, float('-inf')
    for i in range(n):
        st, en, z = map(int, input().split(" "))
        mp[en] = mp.get(en, 0) + z
        end_max = max(end_max, en)
    
    req, prev, mn, mx = sorted(list(mp.items()), key = lambda x: x[0]), 0, float('inf'), float('-inf')

    for it in req:
        cur = math.ceil(it[1]/(it[0]-prev))
        mx = max(mx, cur)
        mn = min(mn, cur)
        prev = it[0]
    
    print(binary(mn, mx, mp, end_max))
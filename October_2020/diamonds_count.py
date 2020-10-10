n = int(input())

#O(log(n, 10))
def calc_n(n):
    e_sm, o_sm = 0, 0
    while n:
        c = n%10
        if c%2:
            o_sm += c
        else:
            e_sm += c
        n //= 10
    return abs(e_sm - o_sm)

tot_sum = 0
last_sum = 0

#O(n*log(n,10))
for i in range(2,n+2):
    last_sum += calc_n(i)

#O(n)
st, en = 2, n+2
for _ in range(n-1):
    tot_sum += last_sum
    last_sum -= calc_n(st)
    last_sum += calc_n(en)
    st += 1
    en += 1

tot_sum += last_sum
print(tot_sum)
#https://www.hackerearth.com/challenges/competitive/october-circuits-20/algorithm/plan-for-nothing-c5768603/


n = int(input())
pw = pow(10,6)

temp = [0]*pw

for _ in range(n):
    ranges = list(map(int, input().split()))
    for i in range(1,len(ranges),2):
        temp[ranges[i]-1] += 1
        if ranges[i+1] < pw:
            temp[ranges[i+1]] -= 1
            
prev = 0
for i in range(pw):
    temp[i] += prev
    prev = temp[i]

print(temp.index(0)+1)
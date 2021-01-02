# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    st = input()
    arr = [st[i: i + 4] for i in range(0, len(st), 4)]

    print(''.join([chr(int(elem,2)+97) for elem in arr]))
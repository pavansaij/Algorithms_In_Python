def makeAnagram(a, b):
    dic = {}
    res = 0
    
    for c1 in a:
        if c1 in dic:
            dic[c1] = dic[c1] + 1
        else:
            dic[c1] = 1
    
    for c in b:
        if c in dic:
            dic[c] = abs(dic[c]-1)
        else:
            res += 1
   
    for key, value in dic.items():
        res += value
      
    return res


a = input()
b = input()
print(makeAnagram(a, b))

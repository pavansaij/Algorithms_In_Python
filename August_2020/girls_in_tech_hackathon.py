'''
Problem Description in the png file named same as this file
'''

def add_one_to_range(array, i, j):
    array[i] += 1

    if j < len(array)-1:
        array[j+1] -= 1

def Optimal_Start_Place_Eval(delays, count):
    possibility_counter = [0]*count

    for i in range(count):
        if delays[i] == 0:
            add_one_to_range(possibility_counter, 0 , count-1)
        elif delays[i] < count:
            if i-delays[i] >= 0:
                add_one_to_range(possibility_counter, 0, i-delays[i])
            
            if i != count-1:
                add_one_to_range(possibility_counter, i+1, count-1 if (i-1) >= delays[i] else min((count-delays[i]+i),count-1))

    cur = 0
    for i in range(count):
        possibility_counter[i] += cur
        cur = possibility_counter[i]

    return possibility_counter.index(max(possibility_counter))

print(Optimal_Start_Place_Eval([1,2,3,0], 4))



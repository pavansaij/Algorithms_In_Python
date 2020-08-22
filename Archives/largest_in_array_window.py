from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, arr, k):
        if k > len(arr):
            return [max(arr)]
        elif k == 1:
            return arr
        
        Qi,n = deque(),len(arr) 
        res = []
        for i in range(k): 
            while Qi and arr[i] >= arr[Qi[-1]] : 
                Qi.pop() 

            Qi.append(i); 
              
        for i in range(k, n): 
            res.append(arr[Qi[0]])
            
            while Qi and Qi[0] <= i-k: 
                Qi.popleft()  
              
            while Qi and arr[i] >= arr[Qi[-1]] : 
                Qi.pop() 
            Qi.append(i)
        res.append(arr[Qi[0]])
        return res
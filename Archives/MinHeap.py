class Min_Heap:
    def __init__(self,heap_in = None):
        if heap_in == None:
            self.heap = []
            self.len  = 0
        else:
            self.heap = heap_in
            self.len  = len(heap_in)

    def parent(self,k):
        return (k-1)//2
    
    def children(self,k):
        return 2*k+1,2*k+2

    def insert(self,data):  
        self.heap.append(data)
        self.len+=1
        self.swim(self.len - 1)
        
    def compare(self,parent,child):
        if self.heap[parent] > self.heap[child]:
            return True
        else:
            return False

    def exchange(self,parent,child):
        self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent] 

    def swim(self,k):
        while (k > 0 and self.compare(self.parent(k),k)):
            self.exchange(self.parent(k),k)
            k = (k-1)//2

    def retrmin(self):
        return self.heap[0]

    def sink(self,k):
        #for single child cases   

        while (2*k+1 and 2*k+2) < (self.len):
            child = 2*k+1
            #check which child of k is highest and set child pointer to that child
            if (child < self.len-1) and (self.heap[child] > self.heap[child+1]):
                child+=1
            if (not self.compare(k,child)):
                break
            self.exchange(k,child)
            k = child
        else:
            if (2*k+2) >= self.len and (2*k+1) < self.len:
                child = 2*k+1
                if (self.compare(k,child)):
                    self.exchange(k,child)
                return 

    def pop(self):
        if self.len == 1:
            self.len-=1
            return self.heap.pop()
        
        if self.heap:
            maxroot = self.heap[0]
            self.exchange(0,self.len-1) 
            self.heap.pop()
            self.len-=1
            self.sink(0)
            return maxroot

minh = Min_Heap()
minh.insert(5)
minh.insert(7)
minh.insert(3)
minh.insert(13)
minh.insert(9)
print(minh.pop())
minh.insert(4)
print(minh.pop())
class WeightedUnion:
    def __init__(self,size):
        self.id = [i for i in range(size)]
        self.wg = [i for i in range(1,size+1)]
        self.rt = [i for i in range(size)]
    
    def union(self,node1,node2):
        root1 = self.root(node1)
        root2 = self.root(node2)
        if root1 == root2:
            return

        if self.wg[node2] > self.wg[node1]:
            self.id[node1] = root2
            self.rt[node1] = root2
            self.wg[root2]+= self.wg[node1]
            self.wg[node1] = self.wg[node2] = self.wg[root2]
        else:
            self.id[node2] = root1
            self.rt[node2] = root1
            self.wg[root1]+= self.wg[node2]
            self.wg[node1] = self.wg[node2] = self.wg[root1]

    def root(self,parent):
        while (parent != self.id[parent]):
            parent = self.id[parent]
        return parent

n, m = map(int, input().split(" "))
tree = WeightedUnion(n)
for _ in range(m):
    x, y = map(int, input().split(" "))
    tree.union(x-1,y-1)
print(tree.id)
print(tree.rt)
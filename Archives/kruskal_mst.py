# cook your dish here
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if(parent[i]==i):
            return i
        return self.find(parent, parent[i])

    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)

        if(rank[xroot] < rank[yroot]):
            parent[xroot] = yroot
        elif(rank[xroot] > rank[yroot]):
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = 0
        i=0
        e=0
        self.graph = sorted(self.graph,key=lambda item:item[2])
        parent,rank = [],[]
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while(e < self.V-1):
            u,v,w = self.graph[i]
            i+=1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if(x != y):
                e+=1
                result += w
                self.union(parent, rank, x, y)
        
        return result
        
def weight(p1, p2):
    res = 0
    for x,y in zip(p1,p2):
        res += abs(x-y)
    return res

n, d = map(int, input().split())
points = []

for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)

g = Graph(0)
count = 0
for i in range(n):
    for j in range(i+1,n):
        g.addEdge(i,j,-weight(points[i], points[j]))
        count += 1
        
print(g.graph)
g.V = count
print(-g.KruskalMST())
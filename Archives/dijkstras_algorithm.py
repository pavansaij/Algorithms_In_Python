import sys
sys.path.append(r'F:\Python\Programs')
from MinHeap import Min_Heap

class Edge():
    def __init__(self,start,target,weight):
        self.start_vertex = start 
        self.target_vertex = target
        self.weight = weight

class Vertex():
    def __init__(self,name,adjacents,mindistance=None):
        self.mindistance = sys.maxsize
        self.visited = False
        self.adjacentlist = adjacents
        self.predecessor = None
        self.name = name
        if mindistance != None:
            self.mindistance = mindistance

    def __gt__(self,other): 
        return self.mindistance > other.mindistance

class Dijkstra():
    def __init__(self,edges_in,vertices_in,start):
        self.vertices = {}
        self.edges = {}
        self.start = start
        self.paths = {}
        self.seen = []

        for vertex in vertices_in:
            if vertex == start:
                self.vertices[vertex] = Vertex(vertex,[],0)
            else:
                self.vertices[vertex] = Vertex(vertex,[])

        for edge in edges_in:
            if edge[0] in self.edges:
                self.edges[edge[0]].append(Edge(self.vertices[edge[0]],self.vertices[edge[1]],edge[2]))
            else:
                self.edges[edge[0]] = [Edge(self.vertices[edge[0]],self.vertices[edge[1]],edge[2])]

        for vertex in vertices_in:
            if vertex in self.edges:
                self.vertices[vertex].adjacentlist = self.edges[vertex]

    def Shortest_Paths(self):
        pq = Min_Heap()
        pq.insert(self.vertices[self.start])

        while pq.heap:
            current_vertex = pq.pop()
            if current_vertex.name not in self.seen:
                for edge in current_vertex.adjacentlist:
                    start_v = edge.start_vertex
                    target_v = edge.target_vertex
                    newDistance = start_v.mindistance + edge.weight
                    if newDistance < target_v.mindistance:
                        target_v.mindistance = newDistance
                        target_v.predecessor = edge.start_vertex
                        self.paths[target_v.name] = target_v
                        pq.insert(target_v)
                        
                self.seen.append(current_vertex.name)

    def cost_of_shortest_path(self,to_vertex):
        if to_vertex in self.paths:
            return self.paths[to_vertex].mindistance
        else:
            raise Exception("No such target_vertex present in the graph")

    def Shortest_path_to(self,to_vertex):
        path = []
        node = self.paths[to_vertex]
        while node:
            path.append(node.name)
            node = node.predecessor
        if path[-1] != self.start:
            return -1
        return path
    
    def Display_path_to(self,to_vertex):
        if to_vertex in self.paths:
            node = self.paths[to_vertex]
            while node:
                print(node.name,end='->')
                node = node.predecessor
        else:
            raise Exception("No such target_vertex present in the graph")
    
nodes,edges_len = map(int,input().strip().split(" "))
edges = []
for _ in range(edges_len):
    st,en,wt = map(str,input().strip().split(" "))
    edges.append([st,en,int(wt)])
vertices = [str(i) for i in range(1,nodes+1)]
dijkstra = Dijkstra(edges,vertices,'1')
dijkstra.Shortest_Paths()
print(dijkstra.Shortest_path_to("7"))
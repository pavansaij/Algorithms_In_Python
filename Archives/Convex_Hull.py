class Convex_Hull():
    def __init__(self):
        self.points = []
        self.stack  = []

    def add_point(self,x,y):
        self.points.append((x,y))
    
    def sort_points(self):
        self.points.sort(key=lambda x: (x[1]))

    def convex_hull(self):
        self.stack.append(self.points[0])
        self.stack.append(self.points[1])
        self.stack.append(self.points[2])


con = Convex_Hull()
n = int(input())
for _ in range(n):
    x,y = map(int, input().split(" "))
    con.add_point(x,y)

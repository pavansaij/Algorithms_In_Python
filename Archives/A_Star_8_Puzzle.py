from MinHeap import Min_Heap

class Board():
    def __init__(self,board,steps):
        self.state = board
        self.g = steps
        self.h = self.h_value()
        self.cost = self.g + self.h
        
    def h_value(self):
        ind = 0
        manhattan_dist = 0
        goal_pos = [-1,[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1]]
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if self.state[ind] != 0 and [i,j] != goal_pos[self.state[ind]]:
                    manhattan_dist+=(abs(goal_pos[self.state[ind]][0]-i)+abs(goal_pos[self.state[ind]][1]-j))
    

class puzzle():
    def __init__(self,)
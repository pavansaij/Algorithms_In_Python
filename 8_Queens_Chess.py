import copy

def Get_Input_Size():
    #N = int(input())
    N = 5
    if N <= 3:
        print("Please enter value greater than this,no possible solutions")
        exit(0)
    return N
    
global N
global solutions
global psblt
psblt = []
solutions = []
N = Get_Input_Size()

def Get_init_Board(N):
    board = []
    for _ in range(N):
        sub = []
        for _ in range(N):
            sub.append(0)
        board.append(sub)
    return board
    
def print_solutions(solutions, size):
    """Prints all the solutions"""
    for sol in solutions:
        for row in sol:
            print(row)
        print(" ")
        
def Check_If_Fits(row,board,col):
    #To chech if any queen is placed on left 
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    #To Check the diagonal                            
    for (i,j) in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    
    #To Check if there is any queen in upway or down            
    for (i,j) in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def Get_Q_Filled(col,board):
        if col >= N:
            return True

        for i in range(N):
            if Check_If_Fits(i,board,col) == True:
                board[i][col] = 1
                if col == N-1:
                   add_solution(board)
                   board[i][col] = 0
                   return
               
                #Recursion    
                Get_Q_Filled(col+1,board)
                board[i][col] = 0
        return False
        
def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)
    
col = 0
#Fills an 0 valued n*n board
board = Get_init_Board(N)
#Driver Code
Get_Q_Filled(col,board)

print("No. of possible solutions : ",len(solutions))
print_solutions(solutions, N)  




# Pradnyesh Choudhari
# Mon May 31 19:30:09 2021
# Sudoku Solver. 
# mat = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        #[6, 0, 0, 1, 9, 5, 0, 0, 0], 
        #[0, 9, 8, 0, 0, 0, 0, 6, 0], 
        #[8, 0, 0, 0, 6, 0, 0, 0, 3], 
        #[4, 0, 0, 8, 0, 3, 0, 0, 1], 
        #[7, 0, 0, 0, 2, 0, 0, 0, 6], 
        #[0, 6, 0, 0, 0, 0, 2, 8, 0], 
        #[0, 0, 0, 4, 1, 9, 0, 0, 5], 
        #[0, 0, 0, 0, 8, 0, 0, 7, 9]]
from math import sqrt

def isSafe(i, j, n, N):
    for k in range(N):
        if mat[i][k] == n or mat[k][j] == n:
            return False
        
    row = (i//int(sqrt(N)))*int(sqrt(N))
    col = (j//int(sqrt(N)))*int(sqrt(N))
    
    for k in range(row, row + int(sqrt(N))):
        for m in range(col, col + int(sqrt(N))):
            if mat[k][m] == n:
                return False
    return True
            

def func(i, j, N):
    # Base Condition
    if i == N:
        print(mat)
        return True
    if j == N:
        return func(i+1, 0, N)
    
    if mat[i][j] == 0:         
        for n in range(1, N+1):
            if isSafe(i, j, n, N):
                mat[i][j] = n
                restSolved = func(i, j+1, N)
                if restSolved:
                    return True
                mat[i][j] = 0
        return False
    else:
        return func(i, j+1, N)

mat = [[0, 2, 0, 4, 0, 6, 0, 0, 9], 
       [0, 5, 3, 0, 0, 0, 0, 0, 4], 
       [7, 0, 0, 1, 0, 0, 0, 0, 0], 
       [0, 0, 5, 6, 0, 0, 3, 0, 0], 
       [0, 0, 0, 0, 5, 0, 0, 0, 0], 
       [0, 0, 7, 0, 0, 3, 2, 0, 0], 
       [0, 0, 0, 0, 0, 1, 0, 0, 6], 
       [2, 0, 0, 0, 0, 0, 9, 3, 0], 
       [8, 0, 0, 3, 0, 9, 0, 4, 0]]

func(0,0,9)
# Pradnyesh Choudhari
# Thu Jun  3 01:26:29 2021
# Max Area of Island.
# Recursive Solution.
# Time Complexity O(m*n) Space Complexity O(1).

def func(grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
            return 0
        grid[i][j] = 0    
        return 1 + func(grid, i-1, j) + func(grid, i, j-1) + func(grid, i+1, j) + func(grid, i, j+1)

    
def maxAreaOfIsland(grid):
    ans, n, m = 0, len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            ans = max(ans, func(grid, i, j))
    return ans
        



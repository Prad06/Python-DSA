# Pradnyesh Choudhari
# Sun May 30 14:44:54 2021
# Target Sum Problem.
# Dynammic Programming Approach.

def countSubsetSum(arr, n, sum):
    t =([[0 for i in range(sum + 1)] for i in range(n + 1)]) 
    
    for i in range(n + 1): 
        t[i][0] = 1
          
    for i in range(1, sum + 1): 
         t[0][i]= 0
              
    for i in range(1, n + 1): 
        for j in range(1, sum + 1): 
            if j>=arr[i-1]: 
                t[i][j] = (t[i-1][j] + t[i-1][j-arr[i-1]]) 
            else: 
                t[i][j] = t[i-1][j]
            
    return t[n][sum] 

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

ss = (sum(arr) + target) // 2

ans = countSubsetSum(arr, len(arr), ss)
print(ans)

# Pradnyesh Choudhari
# Tue Jun  1 00:04:30 2021
# Pancake Problem.
# Time Complexity O(n^2) and Space Complexity O(1).

def find_max(arr, i, j):
    max_num = 0
    max_pos = None
    for i in range(i, j+1):
        if arr[i] > max_num:
            max_num = arr[i]
            max_pos = i
    return max_pos

def flip(arr, pos):
    i = 0
    while i <= pos:
        arr[i], arr[pos] = arr[pos], arr[i]
        i+=1
        pos-=1
    return arr
        
def func(arr, i, j):
    if i == j:
        return
    max_pos = find_max(arr, i, j)
    arr = flip(arr, max_pos)
    print(max_pos+1, end= " ")
    arr = flip(arr, j)
    print(j+1, end = " ")
    func(arr, i, j-1)

    
arr = list(map(int, input().split()))
n = len(arr)
func(arr, 0, n-1)


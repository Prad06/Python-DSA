# Pradnyesh Choudhari
# Sat May 29 18:04:53 2021
# Circular loop array.

def nextPos(arr, i):
    return (arr[i] + i + len(arr)) % len(arr)

def CircularLoop(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            continue
        
        slow = i
        fast = i
        while arr[slow] * arr[nextPos(arr, slow)] > 0 and\
                arr[fast] * arr[nextPos(arr, fast)] > 0 and\
                    arr[fast] * arr[nextPos(arr, nextPos(arr, fast))] > 0:
            slow = nextPos(arr, slow)
            fast = nextPos(arr, nextPos(arr, fast))                    
            
            if slow == fast:
                if slow == nextPos(arr, slow):
                    break
                return True
        
        slow = i
        val = arr[slow]
        while val*arr[slow] > 0:
            x = slow
            slow = nextPos(arr, slow)
            arr[x] = 0
    return False            
        
arr = list(map(int, input().split()))
print(CircularLoop(arr))

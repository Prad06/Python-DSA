# Pradnyesh Choudhari
# Sat May 29 21:30:21 2021
# Recursive solution using Hashmap.

def getAns(n):
    numbers = list(str(n))
    sum = 0
    for i in numbers:
        sum+=int(i)**2
    return sum
    
def func(n):
    if n == 1:
        return True
    
    seen = set()
    
    while n not in seen:
        squared = getAns(n)
        seen.add(n)
        if squared == 1:
            return True

    return False        
        
n = int(input())
ans = func(n)
print(ans)


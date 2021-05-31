# Pradnyesh Choudhari
# Mon May 31 15:53:30 2021
# Word Distance 1
# Time Complexity O(n) Space Complexity O(1).

import sys

def func(sent, w1, w2):
    oc1 = None
    oc2 = None
    min_dist = sys.maxsize
    
    for i in range(len(sent)):
        if sent[i] == w1:
            oc1 = i
        if sent[i] == w2:
            oc2 = i
        print(oc1, oc2, min_dist)
        if oc1 != None and oc2 != None:
            min_dist = min(min_dist, abs(oc1 - oc2))
    
    return min_dist
        

sent = list(input().split(' '))
w1, w2 = map(str, input().split())
ans = func(sent, w1, w2)
print(ans)

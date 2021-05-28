# Pradnyesh Choudhari
# Fri May 28 21:41:45 2021
# Finding Majority Element more than n//3 times.
# Constraints Time O(n) and space O(1).

# Approach 1
# Constraints Time O(n) and space O(n).
# Using Dictionary

from collections import Counter

n = int(input())
arr = map(int, input().split())
count = Counter(arr)
for key, value in count.items():
    if value > (n//3):
        print(key, end = " ")
        
# Approach 2
# Constraints Time O(n) and space O(1).
 


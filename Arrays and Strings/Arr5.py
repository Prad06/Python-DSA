# Pradnyesh Choudhari
# Sat May 29 19:16:07 2021
# Distribute Candies
# Time Complexity O(n) Space Complexity O(n).

from itertools import combinations

candyType = list(map(int, input().split()))
n = len(candyType)
possibleTypes = set(candyType)
print(min(n//2, len(possibleTypes)))


## Additional question. Print all the possible types of candies.
if n//2 >= len(possibleTypes):
    print(*possibleTypes)
else:
    print(*list(combinations(possibleTypes, n//2)))
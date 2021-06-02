# Pradnyesh Choudhari
# Thu Jun  3 01:31:02 2021
# Recursive - Memoized Solution.
# Time Complexity O(m*n) Space Complexity O(m*n).

def check(s1, s2, s3, len1, len2, len3, mem, p1, p2, p3):
    if p3 == len3:
        if p1 == len1 and p2 == len2:
            return True
        else:
            return False
    
    key = str(p1) + '*' + str(p2) + '*' + str(p3)
    
    if key in mem:
        return mem[key]
    
    if p1 == len1:
        if s2[p2] == s3[p3]:
            mem[key] = check(s1, s2, s3, len1, len2, len3, mem, p1, p2+1, p3+1)
        else:
            mem[key] = False
        return mem[key]
    
    if p2 == len2:
        if s1[p1] == s3[p3]:
            mem[key] = check(s1, s2, s3, len1, len2, len3, mem, p1+1, p2, p3+1)
        else:
            mem[key] = False
        return mem[key]
    
    one = False
    two = False
    if s1[p1] == s3[p3]:
        one = check(s1, s2, s3, len1, len2, len3, mem, p1+1, p2, p3+1)
    if s2[p2] == s3[p3]:
        one = check(s1, s2, s3, len1, len2, len3, mem, p1, p2+1, p3+1)
        
    mem[key] = one or two
    return mem[key]
         
        
def isInterleave(s1, s2, s3):
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)
    
    if len3 != len1 + len2:
        return False
    mem = {}
    return check(s1, s2, s3, len1, len2, len3, mem, 0, 0, 0)

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(isInterleave(s1, s2, s3))

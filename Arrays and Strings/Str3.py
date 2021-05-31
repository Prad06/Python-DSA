# Pradnyesh Choudhari
# Mon May 31 22:18:40 2021
# Longest Palindromic Substring.

def lcs(X, Y, n, m):
    if n == 0 or m == 0:
        return 0
    if X[n-1] == Y[m-1]:
        return 1 + lcs(X, Y, n-1, m-1)
    else:
        return max(lcs(X, Y, n-1, m), lcs(X, Y, n, m-1))
    
string = input()
print(lcs(string, string[::-1], len(string),len(string)))




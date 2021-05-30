# Pradnyesh Choudhari
# Sun May 30 14:55:49 2021
# Overlapping Rectangles

def func():
    x0, y0, x1, y1 = map(int, input().split())
    a0, b0, a1, b1 = map(int, input().split())

    if not(x1<=a0 or y0>=b1 or x0>=a1 or b0>=y1):
        return False
    return True

ans = func()
print(ans)
 


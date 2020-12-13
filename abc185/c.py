from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

L = int(input())

n = L-12
k = 12
if n==0:
    print(1)
    exit()

ans = cmb(n+k-1,n)
print(ans)
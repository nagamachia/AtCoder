from fractions import Fraction
from math import ceil, floor, isqrt
 
X, Y, R = map(Fraction, input().split())
lx = ceil(X-R)
rx = floor(X+R)
X, Y, R = map(lambda x: int(x*10**4), [X, Y, R])
res = 0
for x in range(lx, rx+1):
    L = isqrt(R**2 - (x*10**4 - X)**2)
    res += (Y+L) // 10**4 - (Y-L-1) // 10**4
print(res)
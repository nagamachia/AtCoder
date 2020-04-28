import math
import numpy as np
from operator import mul
from functools import reduce
import time

start = time.time()
def comb(n, r, MOD):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer * pow(denom,MOD-2,MOD)

# def combi(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,a,b = map(int, input().split())
MOD = 10**9+7

if (n==2 and a==1 and b==2) or (n==2 and a==2 and b==1):
    print(0)
else:
    ans = (pow(2,n,MOD))-1-comb(n,a,MOD)-comb(n,b,MOD)
    print(ans%MOD)
end = time.time()
print (end-start)
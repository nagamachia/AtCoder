import math
from functools import reduce
from itertools import product,combinations_with_replacement

def gcd_(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())

ans = 3*K*(K-1) + 1

# for i,j,k in product(range(2,K+1),repeat=3):
#     ans += gcd_(i,j,k)
for i,j,k in combinations_with_replacement(range(2,K+1),3):
    if i==j and j==k:
        ans += i
    elif i==j or j==k or k==i:
        ans += gcd_(i,j,k) * 3
    else:
        ans += gcd_(i,j,k)*6
# for i in range(2,K+1):
#     for j in range(2,K+1):
#         for k in range(2,K+1):
#             ans += gcd_(i,j,k)

print(ans)
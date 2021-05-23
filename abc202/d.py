# from itertools import accumulate
from math import factorial

A,B,K = map(int,input().split())

# comb = [0]*(A+1)
# comb[0] = 1
# comb[1] = B

# for i in range(2,A+1):
#     comb[i] = comb[i-1]*(B+i-1)/i

# combSum = list(accumulate(comb))
# # ans = list("a"*A+"b"*B)
# combSum.reverse()
# ans = ""

# for i in range(A+1):
#     if K <= combSum[i]:
#         ans[B+i-1] = "b"
#         res = K-combSum[i-1]
#     else:
#         ans+="a"

def comb(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

a = A
b = B
ans = ""

while a>0 and b>0:
    acomb = comb(a+b-1,a-1)
    if K <= acomb:
        ans+="a"
        a-=1
    else:
        ans+="b"
        K-=acomb
        b-=1
ans+="a"*a
ans+="b"*b

print(ans)

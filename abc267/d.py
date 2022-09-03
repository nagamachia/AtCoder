import numpy as np

N,M = map(int,input().split())
A = list(map(int,input().split()))
# A = np.array(A)
maxA = max(A)
maxIdx = [i for i, x in enumerate(A) if x == maxA]
A_sort = sorted(A,reverse=True)
A_high = A_sort[:max(M*2,N)]

highIdx = []
for i,x in enumerate(A):
    if x in A_high:
        highIdx.append(i)


l = len(maxIdx)
if l>=M:
    ans = int(A[maxIdx[0]]*M*(M+1)*0.5)
    print(ans)
else:
    print(ans)

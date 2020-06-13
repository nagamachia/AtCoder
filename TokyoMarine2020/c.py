import numpy as np
N,K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    Ad = [1]*N
    for j in list(np.nonzero(A)[0]):
    # for j in range(N):
        for k in range(A[j]):
            if j-k-1>=0:
                Ad[j-k-1]+=1
            if j+k+1<N:
                Ad[j+k+1]+=1
    A = Ad

A = list(map(str, A))
print(" ".join(A))
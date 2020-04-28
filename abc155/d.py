import numpy as np
N,K = list(map(int, input().split()))
A = list(map(int, list(input().split())))
ans = []
for i in range(N-1):
    for j in range(N-i-1):
        ans.append(A[i]*A[i+j+1])
ans = np.sort(np.array(ans))
print(ans[K-1])

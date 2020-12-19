import numpy as np

H,W = map(int,input().split())
A = []
for i in range(H):
    A.append(list(map(int,input().split())))
A = np.array(A)
Amin = np.amin(A)
ans = np.sum(A-Amin)
print(ans)
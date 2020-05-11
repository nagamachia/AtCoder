import numpy as np

N,M,X = map(int, input().split())
CA = []

for i in range(N):
    CA.append(list(map(int, input().split())))

CA = np.array(CA)
CAsum = CA.sum(axis=0)
cmin = CAsum[0]

if np.any(CAsum[1:] < X):
    cmin = -1
else:
    for i in range(2**N):
        casum = np.zeros(M+1)
        for j in range(N):
            if((i >> j) & 1):
                casum += CA[j]
        if np.all(casum[1:] >= X):
            cmin = min(cmin,casum[0])

print(int(cmin))
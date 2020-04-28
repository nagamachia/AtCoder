import numpy as np
H,W,K = map(int, input().split())
S=[]
for i in range(H):
    S.append(list(map(int, list(input()))))
S = np.array(S)
print(S)
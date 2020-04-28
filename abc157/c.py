import numpy as np
N,M = map(int, input().split())
sc = []
for i in range(M):
    sc.append(list(map(int, input().split())))
sc = np.array(sc)
ans = str(10**(N-1))
if sc != np.unique(sc) or [1,0] in sc:
    print(-1)
else:
    for i in M:
        

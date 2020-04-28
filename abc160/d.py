import numpy as np
from scipy.sparse.csgraph import shortest_path

N,X,Y = map(int, input().split())

l1 = np.linspace(1,1,N-1)
l = np.diag(l1,k=1) + np.diag(l1,k=-1)

l[X-1,Y-1] = 1
l[Y-1,X-1] = 1

spath = shortest_path(l,indices=0)

for i in range(N-1):
    ans = int(np.count_nonzero(spath==i+1)/2)
    print(ans)

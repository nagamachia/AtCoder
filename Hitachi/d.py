import numpy as np
from operator import itemgetter
N,T = map(int, input().split())

ab = []
for i in range(N):
    l = list(map(int,input().split()))
    l.append(sum(l))
    ab.append(l)
# ab=[list(map(int,input().split())) for i in range(N)]
# ab = np.array(ab)
# absort = ab[np.argsort(ab[:, 0])[::-1]]
# absort = ab[np.argsort(ab[:, 2])]
ab.sort(key=itemgetter(2,0))

t = 0
n = 0

# print(ab)
for i in range(N):
    t += 1
    t += ab[i][0]*t + ab[i][1]
    if t <= T+0.5:
        n += 1

print (n)
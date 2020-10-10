# import numpy as np

N = int(input())
p = list(map(int,input().split()))

# maxp=200001
maxp=max(p)+2

S = [True]*maxp
minT = 0

for i in range(N):
    S[p[i]]=False
    for j in range(minT,maxp):
        if S[j]:
            print(j)
            minT = j
            break

# S = np.array(list(range(maxp)))

# for i in range(N):
#     S = S[~(S==p[i])]
#     print(S.min())
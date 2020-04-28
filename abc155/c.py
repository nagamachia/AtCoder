import numpy as np
import collections
N = int(input())
S =[]
for i in range(N):
    S.append(input())

c = collections.Counter(S)

num = max(c.values())
l = len(c)

ans=[]

for i in range(l):
    if c.most_common()[i][1] == num:
        ans.append(c.most_common()[i][0])
ans.sort()
for x in ans:
    print(x)

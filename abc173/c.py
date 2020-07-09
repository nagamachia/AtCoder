import numpy as np

H,W,K = map(int, input().split())

def s2n(s):
    if s=='#':
        return 1
    else:
        return 0

c = []

for i in range(H):
    c.append(list(map(s2n,list(input()))))
    # c.append(list(input()))

# mp = np.array(c)
ans = 0

def fill(mp,num,iscolumn):
    if iscolumn==0:
        mp[num]=0
    else:
        mp[:,num-H]=0
    return mp

for i in range(2**(H+W)):
    mp = np.array(c)
    for j in range(H+W):
        if((i>>j)&1):
            mp = fill(mp,j,j>=H)
    if np.sum(mp)==K:
        ans+=1

print(ans)
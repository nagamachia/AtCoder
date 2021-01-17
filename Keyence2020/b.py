import numpy as np

N=int(input())
XL=[]
for i in range(N):
    XL.append(list(map(int,list(input().split()))))
XL=np.asarray(XL)
XLs=XL[np.argsort(XL[:,0])]
right=XLs[0][0]+XLs[0][1]
ans=1
for i in range(N-1):
    if right-(XLs[i+1][0]+XLs[i+1][1])>0:
        right=XLs[i+1][0]+XLs[i+1][1]
    elif XLs[i+1][0]-XLs[i+1][1]-right>=0:
        ans+=1
        right=XLs[i+1][0]+XLs[i+1][1]
print(ans)

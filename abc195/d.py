import numpy as np
N,M,Q = map(int,input().split())
WV=[]
for i in range(N):
    WV.append(list(map(int,input().split())))
X = list(map(int,input().split()))
Query=[]
for q in range(Q):
    Query.append(list(map(int,input().split())))

WV=np.array(WV)
WV_sort=WV[np.argsort(WV[:,1])[::-1]]

# print(X)

for q in range(Q):
    L=Query[q][0]
    R=Query[q][1]
    # print(L,R)

    X_q=X[:L-1].copy()
    X_q.extend(X[R:])
    X_q.sort()
    # print('X_q_0:',X_q)
    ans=0

    I=len(X_q)
    for wv in WV_sort:
        # print('wv:',wv)
        # print('X_q:',X_q)
        for i in range(I):
            # print(i)
            if X_q[i] >= wv[0]:
                ans+=wv[1]
                X_q.pop(i)
                I-=1
                # print('i:',i)
                break

    print(ans)
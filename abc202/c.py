from collections import Counter

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

cntA = Counter(A)
cntC = Counter(C)

ans=0

# cntB={}
# B = [b for b in B if b in cntA.keys()]
# for k,v in cntC.items():
#     cntB[]


for k,v in cntA.items():
    ansk=0
    idx = [i for i,x in enumerate(B) if x==k]
    for i in idx:
        ansk+=cntC[i+1]
    # for i,x in enumerate(B):
    #     if x==k:
    #         ansk+=cntC[i+1]
    ans+=ansk*v


print(ans)
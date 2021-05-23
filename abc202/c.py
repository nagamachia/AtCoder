from collections import Counter,defaultdict

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

cntA = defaultdict(int)
for k,v in Counter(A).items():
    cntA[k] = v

ans=0

# for k,v in cntA.items():
#     ansk=0
#     idx = [i for i,x in enumerate(B) if x==k]
#     for i in idx:
#         ansk+=cntC[i+1]
#     ans+=ansk*v

for c in C:
    ans+=cntA[B[c-1]]

print(ans)
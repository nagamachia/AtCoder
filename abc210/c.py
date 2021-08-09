from collections import defaultdict

N,K = map(int,input().split())

c = list(map(int,input().split()))

cnt = defaultdict(int)

for i in range(K):
    cnt[c[i]]+=1

ans=len(set(c[:K]))
kinds=ans

for i in range(N-K):
    cnt[c[i]]-=1
    if cnt[c[i]]==0:
        kinds-=1
    cnt[c[i+K]]+=1
    if cnt[c[i+K]]==1:
        kinds+=1
    ans = max(ans,kinds)

print(ans)
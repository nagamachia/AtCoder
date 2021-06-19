from collections import Counter

N=int(input())

A = list(map(int,input().split()))

c = sorted(list(Counter(A).values()),reverse=True)

ans=0
l=len(c)
s=sum(c)

if l==N:
    ans=int(N*(N-1)*0.5)
else:
    for i in range(l-1):
        if c[i]==1:
            ans+=int((l-i)*(l-i-1)*0.5)
            break
        else:
            s-=c[i]
            ans+=c[i]*s

print(ans)
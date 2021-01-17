import collections

N,K = map(int,list(input().split()))
a =list(map(int,list(input().split())))

ans = 0

c = collections.Counter(a)
amax = max(a)
ar = min(c[0],K)

for i in range(1,amax+1):
    aron = min(c[i],ar)
    if ar>aron:
        ans += (i)*(ar-aron)
        ar = aron
ans += (i+1)*ar

print(ans)
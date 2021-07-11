N=int(input())

C = list(map(int,input().split()))

C=sorted(C)

mod=10**9+7

ans=1

for i in range(N):
    ans = (ans*((C[i]-i)%mod))%mod

print(ans)
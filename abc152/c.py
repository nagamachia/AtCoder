N=int(input())
P = list(map(int, input().split()))

nmin=P[0]
ans=1
for i in range(N-1):
    if nmin > P[i+1]:
        ans+=1
        nmin=P[i+1]

print(ans)

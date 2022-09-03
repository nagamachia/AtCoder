
N,M = map(int,input().split())
A = list(map(int,input().split()))

s=0
for i in range(M):
    s += A[i]*(i+1)

ans=s
ss=sum(A[:M])
for j in range(N-M):
    if j!=0:
        ss = ss - A[j-1] + A[M+j-1]
    s = s-ss+A[M+j]*M
    ans = max(s,ans)

print(ans)

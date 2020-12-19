N = int(input())

A = list(map(int,input().split()))
A = sorted(A)
ans = 0

for i in range(N):
    ans += (N-1-2*i)*A[N-i-1]

print(ans)
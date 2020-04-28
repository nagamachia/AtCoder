K,N = map(int, input().split())
A = list(map(int, input().split()))

d = K-A[N-1]+A[0]
for i in range(N-1):
    d = max(d,A[i+1]-A[i])

print(K-d)
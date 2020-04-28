N,M = map(int, input().split())
A = list(map(int, input().split()))

sm = sum(A)
if N >= sm:
    print(N-sm)
else:
    print(-1)

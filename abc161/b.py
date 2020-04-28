N,M = map(int, input().split())
A = list(map(int, input().split()))

th = sum(A)*0.25/M

A.sort(reverse=True)

if A[M-1] >= th:
    print('Yes')
else:
    print('No')
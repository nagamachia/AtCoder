H,N = map(int, input().split())
A = map(int, list(input().split()))
if H <= sum(A):
    print('Yes')
else:
    print('No')

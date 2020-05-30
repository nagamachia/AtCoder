N = int(input())
A = list(map(int, input().split()))

apex = 0
node = 1

for i in range(N):
    apex += node
    node = (node - A[i])*2
    if node<0:
        print(-1)
        exit()

apex+=node
maxleaf = node

if maxleaf < A[N]:
    print(-1)
    exit()
elif maxleaf == A[N]:
    print(apex)
    exit()
elif maxleaf > A[N]:
    leaf = maxleaf
    for i in range(N):
        if A[N]>=int((leaf-A[N-i])*0.5):
            apex -= leaf-A[N]
            print(apex)
            exit()
        leaf = int((leaf-A[N-i])*0.5)
        apex -= int((leaf+A[N-i])*0.5)
    print(-1)


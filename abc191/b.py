N,X = map(int,input().split())
A = list(map(int,input().split()))
Ad = []

for i in range(N):
    if A[i]!=X:
        Ad.append(A[i])

Ad = ' '.join(map(str,Ad))
print(Ad)
N,X=map(int,input().split())

A = list(map(int,input().split()))

discount=int(N/2)

price=sum(A)-discount

if X>=price:
    print("Yes")
else:
    print("No")

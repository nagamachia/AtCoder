from collections import Counter

N=int(input())

A=list(map(int,input().split()))

c=Counter(A)

if c.most_common()[0][1] > 1:
    print("No")
else:
    print("Yes")

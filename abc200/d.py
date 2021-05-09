from itertools import product
from collections import Counter

N = int(input())
A = list(map(lambda x: int(x)%200, input().split()))

sums = []

bins = list(product([False, True], repeat=min(N,8)))[1:]

for b in bins:
    s=0
    for i in range(min(N,8)):
        if b[i]:
            s+=A[i]
    sums.append(s%200)

if max(Counter(sums).values())<2:
    print("No")
else:
    print("Yes")
    for k,v in Counter(sums).items():
        if v>=2:
            pair = [i for i, s in enumerate(sums) if s==k][:2]
            for p in pair:
                x = sum(bins[p])
                B = [i+1 for i, b in enumerate(bins[p]) if b]
                print(x,*B)
            exit()


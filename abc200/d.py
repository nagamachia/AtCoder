import itertools as itrt

N = int(input())
A = int(input().split())

sums = []
ls = []

for i in range(1,N):
    for l in itrt.combinations(A, i):
        ls.append(l)
        s = sum(l)%200
        if s in set(sums):
            sums[sums.index(s)]
        sums.append()

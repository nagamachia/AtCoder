import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
ans = [0]*N

for ci in c.items():
    ans[ci[0]-1]=ci[1]

for i in ans:
    print(i)
import collections
N,K = map(int, input().split())
d=[]
A = []

for i in range(K):
    d.append(input())
    A.extend(list(map(int, input().split())))

c = collections.Counter(A)

print(N-len(c))
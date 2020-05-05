# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         if self.parents[x] > self.parents[y]:
#             x, y = y, x

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         return {r: self.members(r) for r in self.roots()}

#     def __str__(self):
#         return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
N,M = map(int, input().split())
H = list(map(int, input().split()))
AB = []
# uf = UnionFind(N)
dic = {}
ansl = []

for i in range(M):
    ab = list(map(int, input().split()))
    # ab[0] -= 1
    # ab[1] -= 1
    # uf.union(*ab)
    AB.extend(ab)
    # ansl.append(max([H[ab[0]-1],H[ab[0]-1]]))
    dic.setdefault(ab[0],[]).append(ab[1])
    dic.setdefault(ab[1],[]).append(ab[0])

# print(dic)
# print(uf.all_group_members())
# ans = len(set(ansl))
ans = N-len(set(AB))
for k,v in dic.items():
    if H[k-1] > max(list(map(lambda x: H[x-1], v))):
        ans += 1

print(ans)


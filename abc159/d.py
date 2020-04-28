import collections

N = int(input())

A = list(map(int, input().split()))

c = collections.Counter(A)
# print(c)
# dic = {}
ans = 0
# for k,v in c.items():
#     dic[k] = int(v*(v-1)/2)
# print(dic)
for v in c.values():
    ans += int(v*(v-1)/2)

for k in range(N):
    Ak = A[k]
    cAk = c[Ak]
    ansk = ans - cAk + 1
    # ans[Ak] = int((cAk-1)*(cAk-2)/2)
    # print(dic,ans)
    print(ansk)
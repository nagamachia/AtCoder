import numpy as np
N,M,Q = map(int, input().split())

# abcd = np.array([[None,None,None,None]])
abcd = []

for i in range(Q):
    abcd.append(list(map(int, input().split())))
    # abcd = np.append(abcd, list(map(int, input().split())), axis=0)

abcd = np.array(abcd)
# print(abcd)

abcd_s = abcd[np.argsort(abcd[:, 3])[::-1]]
# print(abcd_s)
# A = [1]*N

ans = 0

mat = np.zeros((Q,N))
# mat = np.arange(Q*N).reshape(Q,N)
# print(mat)
for i in range(Q):
    # print(abcd[i,0])
    mat[i,abcd[i,0]-1] = -1
    mat[i,abcd[i,1]-1] = 1

rank = np.linalg.matrix_rank(mat)
# A[]
ans = sum(abcd[:rank,3])

print(ans)
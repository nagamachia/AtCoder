from itertools import permutations

S,K = input().split()
K=int(K)

ans = ''.join(sorted(list(set(permutations(list(S)))))[K-1])

print(ans)

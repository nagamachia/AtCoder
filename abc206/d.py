from collections import Counter
from itertools import chain

N=int(input())
A = list(map(int,input().split()))

not_circ = []

# for i in range(N//2):
#     if A[i]!=A[N-1-i]:
#         not_circ.extend([A[i],A[N-1-i]])

# c = Counter(not_circ)
# l=len(c)
# if l==0:
#     print(0)
# else:
#     print(l-1)

for i in range(N//2):
    if A[i]!=A[N-1-i]:
        not_circ.append([A[i],A[N-1-i]])

not_circ_flatten = list(chain.from_iterable(not_circ))


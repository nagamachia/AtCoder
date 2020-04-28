from itertools import product
N = int(input())
S = input()

ans = 0
R = [i for i, x in enumerate(S) if x == 'R']
G = [i for i, x in enumerate(S) if x == 'G']
B = [i for i, x in enumerate(S) if x == 'B']

for i,j,k in product(R,G,B):
    ijk = sorted([i,j,k])
    if (ijk[1]-ijk[0]) != (ijk[2]-ijk[1]):
        ans += 1
print(ans)
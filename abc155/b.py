import sys
N = int(input())
A = list(map(int, list(input().split())))
E = []
for i in range(N):
    if A[i]%2 == 0:
        E.append(A[i])
if len(E) == 0:
    print('APPROVED')
else:
    for j in range(len(E)):
        if E[j]%3 != 0 and E[j]%5 != 0:
            print('DENIED')
            sys.exit()
    print('APPROVED')

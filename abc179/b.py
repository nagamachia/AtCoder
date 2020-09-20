N = int(input())

D = []

for i in range(N):
    D.append(input().split())

mxn = 0
num = 0

for i in range(N):
    if D[i][0]==D[i][1]:
        num += 1
        mxn = max(num,mxn)
    else:
        num = 0

if mxn >= 3:
    print('Yes')
else:
    print('No')
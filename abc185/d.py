import math
N,M = map(int,input().split())
A = list(map(int,input().split()))
if M==0:
    print(1)
    exit()
if N==M:
    print(0)
    exit()
A_sort = sorted(A)
dsts =[]
def add_dsts(dst,dsts):
    if dst>0:
        dsts.append(dst)
    return dsts
dsts = add_dsts(A_sort[0]-1,dsts)

for i in range(M-1):
    dst=A_sort[i+1]-A_sort[i]-1
    dsts=add_dsts(dst,dsts)
dsts = add_dsts(N-A_sort[M-1],dsts)

k = min(dsts)
# print("dsts",dsts)
ans = 0
for dst in dsts:
    ans+=math.ceil(dst/k)
print(ans)
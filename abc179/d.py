N,K = map(int,input().split())

LR = []
S = []
mod = 998244353

for i in range(K):
    LR.append(list(map(int,input().split())))
    S = S+list(range(LR[i][0],LR[i][1]+1))

dst = N-1

print(S)

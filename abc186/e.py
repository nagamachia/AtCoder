T = int(input())
Ans=[]
for t in range(T):
    N,S,K = map(int,input().split())
    if N%K==0:
        if S%K==0:
            ans = int((N-S)/K)
            Ans.append(ans)
        else:
            Ans.append(-1)
    else:
        mod=(S%K)%(N%K)
        if mod == 0:
            ans = int((N-S)/K)
            Ans.append(ans)
        else:
            ans = int(((mod%K)*N-S)/K)
            Ans.append(ans)
for a in Ans:
    print(a)


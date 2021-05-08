N,K = map(int,input().split())
divflg=False

for i in range(K):
    if divflg:
        if N%2==0:
            N/=2
        else:
            N=N*10+2
    elif N%200==0:
        N=N/200
        divflag=True
    else:
        N=N*1000+200

print(int(N))
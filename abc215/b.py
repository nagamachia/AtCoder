import math

N=int(input())

ans=int(math.log2(N))
tmp=2**(ans+1)

if tmp<=N:
    print(ans+1)
elif int(tmp*0.5)<=N:
    print(ans)
else:
    print(ans-1)


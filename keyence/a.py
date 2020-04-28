import math
H=int(input())
W=int(input())
N=int(input())

num=max([H,W])
ans=int(math.ceil(N/float(num)))

print(ans)

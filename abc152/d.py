import math
import numpy as np
N=int(input())
num=[1,2,3,4,5,6,7,8,9]
dig=int(math.log10(N))
case=np.ones((9,9))
for h in num:
    for t in num:
        base=h*(10**dig)+t
        # print(base,base+10**dig-9)
        ls=np.arange(base,base+10**dig-9)
        ls=ls[ls<=N]
        print(ls)
        case[h-1,t-1]=len(ls)
        if h==t:
            case[h-1,t-1]+=1
print(case)
ans=np.sum(np.dot(case,case))

print(ans)

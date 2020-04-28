import numpy as np
def fast_argmin(array):
    array = list( array )
    return array.index(min(array))
def fast_gNV(list, num):
    idx = fast_argmin(np.abs(np.asarray(list) - num))
    return list[idx]
#def gNV(list, num):
#    idx = np.abs(np.asarray(list) - num).argmin()
#    return list[idx]

N=int(input())
A=[int(x) for x in input().split()]
Asum=[]
for i in range(N):
    Asum.append(sum(A[:i+1]))
Amax=Asum[-1]
Ahalf=Amax/2.0
if Ahalf.is_integer() and int(Ahalf) in set(Asum):
    ans=0
else:
    ANV=fast_gNV(Asum, Ahalf)
    #ANV=Asum[np.abs(np.asarray(Asum)-Ahalf).argmin()]
    ans=abs(2*ANV-Amax)
print(ans)    

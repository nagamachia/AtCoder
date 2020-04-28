import math
from collections import Counter
N=int(input())
D=input().split()
T=[]
D_dict=Counter(D)
D_keys=list(D_dict.keys())
D_keyi=[int(n) for n in D_keys]
maxD=max(D_keyi)
D_keyi.sort()
ans=1
if D[0] != '0' or D_dict['0']!=1 or D_keyi != list(range(maxD+1)):
    print(0)
else:
    for i in range(maxD+1):
        T.append(D_dict[str(i)])
    for i in range(len(T)-1):
        ans=ans*(T[i]**T[i+1])
    print((ans%998244353))

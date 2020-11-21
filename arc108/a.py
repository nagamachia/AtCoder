import math

S,P = map(int,input().split())

M = int((S+math.sqrt(S**2-4*P))*0.5)

N = int((S-math.sqrt(S**2-4*P))*0.5)

if (N+M)==S and N*M==P:
    print("Yes")
else:
    print("No")
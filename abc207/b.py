import math

A,B,C,D=map(int,input().split())

cdb=C*D-B
if cdb<=0:
    ans=-1
else:
    ans=math.ceil(A/cdb)

print(ans)
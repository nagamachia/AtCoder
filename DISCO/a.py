import math
X,Y=input().split()
X=int(X)
Y=int(Y)
prize = [0]*206
prize[1:4] = [300000,200000,100000]
#print(prize)
if X==1 and Y==1:
    ans=1000000
else:
    ans=prize[X]+prize[Y]

print(ans)

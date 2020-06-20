import math

X = int(input())
deg = 360

if deg%X==0:
    ans = deg//X
else:
    ans = ((deg*X)//math.gcd(deg,X))//X

print(ans)
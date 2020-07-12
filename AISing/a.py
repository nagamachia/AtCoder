import math

L,R,d = map(int, input().split())

Li = math.ceil(L/d)
Ri = int(R/d)

ans = Ri-Li+1

print(ans)
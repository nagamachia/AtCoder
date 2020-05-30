import math
A,B,H,M = map(int, input().split())

ans = math.sqrt(A**2+B**2-2*A*B*math.cos(math.pi*(60*H-11*M)/360))

print(ans)
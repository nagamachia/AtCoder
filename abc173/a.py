import math

N = int(input())

n = math.ceil(N/1000)

ans = n*1000 - N

print(ans)
import math

N = int(input())

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

cur_lcm = 2

if N==2:
    ans = 3
else:
    for i in range(3,N+1):
        cur_lcm = lcm(cur_lcm,i)
    ans = cur_lcm + 1

print(ans)
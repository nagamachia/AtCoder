import math

N = int(input())
T = input()

minT = int(math.ceil(N/3))

num = 10**10

ans = 0


if N == 1 and T == "1":
    ans = num*2
elif T in "110"*(minT-1):
    ans = num-minT+2
elif T in "110"*minT:
    ans = num-minT+1
elif T in "110"*(minT+1):
    ans = num-minT

print(ans)

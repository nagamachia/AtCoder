import math
def intpow(X):
    return int(X*1.01)

X = int(input())

ans = math.ceil((math.log(X)-2*math.log(10))/math.log(1.01))

# X0 = 100
Xn = 100
for i in range(ans):
    Xn = int(Xn*1.01)
    # print(Xn)

while X > Xn:
    Xn = int(Xn*1.01)
    ans += 1

print(ans)
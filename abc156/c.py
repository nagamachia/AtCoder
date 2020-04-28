import math
N = int(input())
X = list(map(int, input().split()))

Xm = sum(X)/N
Xmi = int(Xm)
Xmc = math.ceil(Xm)

Si = list(map(lambda x:(x-Xmi)**2, X))
Sc = list(map(lambda x:(x-Xmc)**2, X))

ans = min([sum(Si),sum(Sc)])
print(ans)
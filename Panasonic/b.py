import math
H,W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
elif H%2 == 0:
    print(int(H/2*W))
elif W%2 == 0:
    print(int(W/2*H))
else:
    ans = H*(int(W/2))+math.ceil(H/2)
    print(int(ans))
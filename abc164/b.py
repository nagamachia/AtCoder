import math

A,B,C,D = map(int, input().split())

tn = math.ceil(C/B)
an = math.ceil(A/D)

if tn <= an:
    print("Yes")
else:
    print("No")
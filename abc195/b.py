import math
A,B,W = map(int,input().split())
W=W*1000
if A>W:
    print("UNSATISFIABLE")
else:
    minO = math.ceil(W/B)
    maxO = int(W/A)
    if minO*A<=W and W<=minO*B:
        print(minO,maxO)
    else:
        print("UNSATISFIABLE")

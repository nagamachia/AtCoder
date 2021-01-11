X,Y = map(int,input().split())

d = abs(X-Y)
if d<3:
    print("Yes")
else:
    print("No")
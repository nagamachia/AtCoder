X,Y = map(int, input().split())

k = Y-2*X
t = 4*X-Y

if Y%2==0 and k>=0 and t>=0:
    print("Yes")
else:
    print("No")


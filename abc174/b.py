N,D = map(int, input().split())

# XY = []
ans = 0
D2=D**2

for i in range(N):
    # XY.append(list(map(int, input().split())))
    X,Y = map(int, input().split())
    if X**2+Y**2<=D2:
        ans+=1

print(ans)
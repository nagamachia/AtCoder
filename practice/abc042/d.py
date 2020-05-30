N,K = map(int, input().split())
A = list(map(int, input().split()))

loc = 1
loclog=[1]
flag = 0
hist = [0]*N

for i in range(K):
    hist[loc-1] = 1
    loc = A[loc-1]
    if hist[loc-1] != 0:
        roopstart = loclog.index(loc)
        roopend = len(loclog)
        flag = 1
        break
    loclog.append(loc)

if flag == 0:
    ans = loc
else:
    roopidx = (K+1-roopstart)%(roopend-roopstart)
    if roopidx == 0:
        ans = loclog[roopend-1]
    else:
        ans = loclog[roopstart+roopidx-1]
print(ans)
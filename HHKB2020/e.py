def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

N = int(input())

xy = []

for i in range(N):
    xy.append(list(map(int,input().split())))

# xy = get_unique_list(xy)
# N = len(xy)
ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        ans = max(abs(xy[i][0]-xy[j][0])+abs(xy[i][1]-xy[j][1]),ans)

print(ans)
N,M = map(int,input().split())
AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))

K = int(input())
CD = []
for i in range(K):
    CD.append(list(map(int,input().split())))

ans = 0

for i in range(2**K):
    dish = [0]*N
    for k in range(K):
        if ((i>>k) & 1):
            dish[CD[k][1]-1]+=1
        # else:
        elif ((i>>k) & 1)==0:
            dish[CD[k][0]-1]+=1
    case = 0
    for m in range(M):
        if dish[AB[m][0]-1]>=1 and dish[AB[m][1]-1]>=1:
            case += 1
    ans = max(ans,case)

print(ans)
N=int(input())

tlr=[]

for i in range(N):
    tlr.append(list(map(int,input().split())))

tlr=sorted(tlr, key=lambda x: x[1])

ans=0

for i in range(N-1):
    for j in range(i+1,N):
        if tlr[i][0]%2==0 or tlr[j][0]>=3:
            if tlr[i][2]>tlr[j][1]:
                ans+=1
        else:
            if tlr[i][2]>=tlr[j][1]:
                ans+=1

print(ans)


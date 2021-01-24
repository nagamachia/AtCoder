N,X = map(int,input().split())
alc = 0
VP = []
for i in range(N):
    V,P = map(int,input().split())
    VP.append([V,P])

for i in range(N):
    alc += VP[i][0]*VP[i][1]
    if alc > X*100:
        print(i+1)
        exit()
print(-1)

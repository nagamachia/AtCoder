H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())

for i in range(1,H-1):
    for j in range(1,W-1):
        if S[i-1][j]=='.' and S[i][j]=='#':
            start_i = i
            start_j = j
            break

ans = 0

i = start_i
j = start_j + 1
mode = 0
while i!=start_i or j!=start_j or mode!=0:
    while mode==0:
        if S[i-1][j]=='.' and S[i][j]=='#':
            j+=1
        elif S[i-1][j]=='.' and S[i][j]=='.':
            mode = 1
            ans+=1
            j-=1
            continue
        elif S[i-1][j]=='#' and S[i][j]=='#':
            mode = 3
            ans+=1
            i-=1
            continue
    while mode==1:
        if S[i][j+1]=='.' and S[i][j]=='#':
            i+=1
        elif S[i][j+1]=='.' and S[i][j]=='.':
            mode = 2
            ans+=1
            i-=1
            continue
        elif S[i][j+1]=='#' and S[i][j]=='#':
            mode = 0
            ans+=1
            j+=1
            continue
    while mode==2:
        if S[i+1][j]=='.' and S[i][j]=='#':
            j-=1
        elif S[i+1][j]=='.' and S[i][j]=='.':
            mode = 3
            ans+=1
            j+=1
            continue
        elif S[i+1][j]=='#' and S[i][j]=='#':
            mode = 1
            ans+=1
            i+=1
            continue
    while mode==3:
        if S[i][j-1]=='.' and S[i][j]=='#':
            i-=1
        elif S[i][j-1]=='.' and S[i][j]=='.':
            mode = 0
            ans+=1
            i+=1
            continue
        elif S[i][j-1]=='#' and S[i][j]=='#':
            mode = 2
            ans+=1
            j-=1
            continue


print(ans)


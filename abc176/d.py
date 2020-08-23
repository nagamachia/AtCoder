from collections import deque

H,W = map(int, input().split())
Ch,Cw = map(int, input().split())
Dh,Dw = map(int, input().split())

S = []
for i in range(H):
    S.append(list(input()))

S[Ch-1][Cw-1]=0
que = deque([[Ch-1,Cw-1]])

while que:
    y,x = que.popleft()
    for j,i in [(1,0),(0,1),(-1,0),(0,-1)]:
        nexty,nextx = y+j, x+i
        if nexty>=0 and nexty<H and nextx>=0 and nextx<W:
            dist = S[nexty][nextx]
            if dist!='#':
                if dist=='.':
                    S[nexty][nextx] = S[y][x]
                    que.append([nexty,nextx])
                elif dist>S[y][x]:
                    S[nexty][nextx] = S[y][x]
                    que.append([nexty,nextx])
            else:
                for jj,ii in [(2,-2),(2,-1),(2,0),(2,1),(2,2),(1,-2),(1,-1),(1,1),(1,2),(0,-2),(0,2),(-1,-2),(-1,-1),(-1,1),(-1,2),(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2)]:
                    nextyy,nextxx = y+jj, x+ii
                    if nextyy>=0 and nextyy<H and nextxx>=0 and nextxx<W:
                        distt = S[nextyy][nextxx]
                        if dist!='#':
                            if dist=='.':
                                S[nextyy][nextxx] = S[y][x]+1
                                que.append([nextyy,nextxx])
                            elif dist>S[y][x]:
                                S[nextyy][nextxx] = S[y][x]+1
                                que.append([nextyy,nextxx])

print(S)
print(S[Dh-1][Dw-1])
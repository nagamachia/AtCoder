import numpy as np
from collections import deque

def bfs(maze, cost, sy, sx):
    queue = deque([[sy, sx]])
    cost[sy][sx] = 0
    # ans = N**2
    while queue:
        y, x = queue.popleft()
        if y==1 or x==1 or y==N or x==N:
            return cost[y][x]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y+j, x+k
            if maze[new_y][new_x] == 0 and cost[new_y][new_x] > cost[y][x]:
                cost[new_y][new_x] = cost[y][x]
                queue.append([new_y, new_x])
            elif maze[new_y][new_x] == 1 and cost[new_y][new_x] > cost[y][x]+1:
                cost[new_y][new_x] = cost[y][x]+1
                queue.append([new_y, new_x])
            # else:
            #     queue.append([new_y, new_x])

N = int(input())
P = list(map(int, input().split()))
order = [0]*(N**2)
for i in range(N**2):
    order[P[i]-1] = i+1

maze = np.ones((N+2,N+2))
maze[0]=0
maze[:,0]=0
maze[-1]=0
maze[:,-1]=0
cost = np.ones((N+2,N+2))
cost[:] = N**2

ans = 0
print(cost)

for o in order:
    mod = o%N
    sy = int(o/N)+1
    if mod==0:
        sx = N
    else:
        sx = mod
    ans += bfs(maze,cost,sy,sx)
    print(bfs(maze,cost,sy,sx))
    maze[sy][sx]=0

print(int(ans))
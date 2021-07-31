from collections import deque

N,M = map(int,input().split())

AB = [list(map(int,input().split())) for i in range(M)]

graph = [[] for _ in range(N+1)]

for i in range(M):
 a, b = map(int, input().split())
 graph[a].append(b)
 graph[b].append(a)

dist = [-1] * (N+1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
 v = d.popleft()
 for i in graph[v]:
   if dist[i] != -1:
     continue
   dist[i] = dist[v] + 1
   d.append(i)

ans = dist[1:]
print(*ans, sep="\n")
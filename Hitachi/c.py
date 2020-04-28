N = int(input())
edges = []
for i in range(N-1):
    edges.append(input().split())

def BFS(edges,N):
  roots=[ [] for i in range(N)]
  c = 1
  for a,b in edges:
    roots[a-1]+=[(b-1,c)]
    roots[b-1]+=[(a-1,c)]
  dist=[-1]*N
  stack=[]
  stack.append(K)
  dist[K]=0
  while stack:
    label=stack.pop(-1)
    for i,c in roots[label]:
      if dist[i]==-1:
        dist[i]=dist[label]+c
        stack+=[i]
  return dist
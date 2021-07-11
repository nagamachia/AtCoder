N = int(input())
s_list = [input() for _ in range(N)]
 
nodes = set()
for s in s_list:
    nodes.add(s[:3])
    nodes.add(s[-3:])
 
nodes_to_v = {s: v for v, s in enumerate(nodes)}
V = len(nodes_to_v)
 
deg = [0] * V
adj = [[] for _ in range(V)]
for s in s_list:
    u = nodes_to_v[s[:3]]
    v = nodes_to_v[s[-3:]]
    deg[u] += 1
    adj[v].append(u)
 
stack = []
state = [2] * V # 0: lose, 1: win, 2: draw
for r in range(V):
    if deg[r] == 0:
        stack.append(r)
        state[r] = 0
 
while stack:
    v = stack.pop()
    for nv in adj[v]:
        deg[nv] -= 1
        if state[nv] != 2:
            continue
        if state[v] == 0:
            state[nv] = 1
            stack.append(nv)
        elif deg[nv] == 0:
            state[nv] = 0
            stack.append(nv)
 
convert = ["Takahashi", "Aoki", "Draw"]
 
ans = []     
for s in s_list:
    print(convert[state[nodes_to_v[s[-3:]]]])
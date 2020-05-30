import numpy as np
from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacent = []

def bfs(root):
    if root is None:
        return 
    q = deque()
    visit(root)
    q.append(root)
    while q:
        r = q.popleft()
        for n in r.adjacent:
            if not n.visited:
                visit(n)
                q.append(n)

def visit(node):
    print(f"ノード：{node.name}")
    # print(f"隣接：{node.adjacent}")
    node.visited = True

N,M = map(int, input().split())
AB = []

for i in range(M):
    AB.append(list(map(int, input().split())))

# AB = np.array(AB)

# print(AB)

gragh = {}

for ab in AB:
    gragh.setdefault(ab[0], []).append(ab[1])
    gragh.setdefault(ab[1], []).append(ab[0])

# print(gragh)

# ノードを作成
n = []
for i in range(N):
    n.append(Node(str(i+1)))

# ノード間を隣接させる
for k,v in gragh.items():
    n[k-1].adjacent = [n[x-1] for x in v]

bfs(n[0])


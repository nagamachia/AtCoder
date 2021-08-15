import numpy as np
 
N = int(input())
 
S = list(map(int,input().split()))
T = list(map(int,input().split()))
 
# S = S*2
 
idx = [i for i in range(N)]*2
 
 
t_table = [[0]*N]*N
# t_table = np.array(t_table)
 
for i in range(N):
    t_table[i][i] = T[i]
    for j in range(i,i+N-1):
        t_table[i][idx[j+1]] = t_table[i][idx[j]] + S[idx[j]]
 
t_table_min=t_table.min(axis=0)
 
for j in range(N):
    print(t_table_min[j])
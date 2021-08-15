N = int(input())
 
S = list(map(int,input().split()))
T = list(map(int,input().split()))

t_table = T

for i in range(2*N):
    t_table[(i+1)%N] = min(t_table[i%N]+S[i%N], T[(i+1)%N])

for i in range(N):
    print(t_table[i])

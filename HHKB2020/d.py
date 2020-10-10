T = int(input())
mod = 1000000007

for t in range(T):
    N,A,B = map(int,input().split())
    ans = (N-A+1)**2*(N-B+1)**2
    

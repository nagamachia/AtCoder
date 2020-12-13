N,M,T = map(int,input().split())
AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))

n = N
t = 0

def judge(n):
    if n<=0:
        print("No")
        exit()

for ab in AB:
    n=n-(ab[0]-t)
    judge(n)
    n=min(n+(ab[1]-ab[0]),N)
    t=ab[1]

n=n-(T-ab[1])
judge(n)
print("Yes")
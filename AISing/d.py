N = int(input())
X = input()

def f(n):
    return int(''.join(n),2)%(n.count("1"))

tb = [None]*N

for i in range(N):
    ans = 0
    Xi = list(X)
    if Xi[i]=="0":
        Xi[i]="1"
    else:
        Xi[i]="0"
    vXi = Xi
    # pc = Xi.count("1")
    while(vXi.count("1")!=0):
        if tb[]
        vXi = format(f(vXi),'b')
        ans += 1
    tb[int(''.join(Xi),2)-1]=ans
    print(ans)
    
    
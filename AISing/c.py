import math

N = int(input())

rs = []
ans = [0]*N

maxn = math.ceil(math.sqrt(N))

def f(x,y,z):
    return x**2+y**2+z**2+x*y+y*z+z*x

for i in range(1,maxn+1):
    for j in range(1,maxn+1):
        for k in range(1,maxn+1):
            result = f(i,j,k)
            if result>N:
                break
            ans[result-1]+=1
            # rs.append(i,j,k)

for a in ans:
    print(a)
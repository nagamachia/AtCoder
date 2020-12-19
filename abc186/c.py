N = int(input())
N10 = str(N)
N8 = oct(N)

ans = 0
for i in range(1,N+1):
    if '7' in str(i)+oct(i):
        continue
    ans+=1
print(ans)
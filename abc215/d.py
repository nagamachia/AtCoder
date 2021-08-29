N,M = map(int,input().split())
A = list(map(int,input().split()))
maxA = max(max(A),M)

k = [True]*(maxA+1)
isPrime = [True]*(maxA+1)
prime = []

for a in A:
    k[a] = False

for i in range(2,maxA+1):
    if not isPrime[i]:
        continue
    for j in range(i*2,maxA+1,i):
        isPrime[i] = False
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

for p in prime:
    for j in range(p*2,M+1,p):
        # k[j] = k[j] * k[p]
        k[j] = False

ans = [1]

for i in range(2,M+1):
    if k[i]:
        ans.append(i)


print(len(ans))
for a in ans:
    print(a)


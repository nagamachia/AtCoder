N = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = [0]*N
c[0] = a[0]*b[0]
amax = a[0]
print(c[0])
for n in range(1,N):
    amax = max(amax,a[n])
    c[n] = max([c[n-1],b[n]*amax])
    print(c[n])
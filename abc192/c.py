N,K = map(int,input().split())
a = N

def f(x):
    g1 = int(''.join(sorted(str(x),reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1-g2

for i in range(K):
    a = f(a)


print(a)
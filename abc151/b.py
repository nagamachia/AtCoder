N,K,M = map(int, input().split())
A = map(int, input().split())

res = N*M - sum(A)

if res < 0:
    print ('0')
elif res <= K:
    print (res)
else:
    print('-1')

N,A,B = map(int, input().split())

if A == 0:
    print(0)
# elif N <= A:
#     print(N)
# elif N < (A+B):
#     print(A)
elif N < (A+B):
    print(min(A,N))
else:
    div = int(N/(A+B))
    quob = min(N%(A+B),A)
    ans = div*A+quob
    print(ans)
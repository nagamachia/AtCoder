A,B,C,K = map(int, input().split())

if K <= A:
    ans = K
elif A+B >= K:
    ans = A
else:
    ans = 2*A+B-K

print(ans)
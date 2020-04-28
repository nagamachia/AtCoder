N,K = map(int, input().split())
H = list(map(int, input().split()))
if N <= K:
    ans = 0
else:
    H.sort()
    H.reverse()
    ans = sum(H[K:])

print(ans)

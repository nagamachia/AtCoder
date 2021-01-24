N = int(input())
S=[""]*N

for i in range(N):
    S[i] = input()

ans = 0

for i in reversed(range(N)):
    if S[i]=="OR":
        ans += 2**(i+1)

ans+=1

print(ans)
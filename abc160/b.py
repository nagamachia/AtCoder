X = int(input())
ans = 0

p500 = int(X/500)

X -= p500*500

p5 = int(X/5)

ans = p500*1000 + p5*5

print(ans)
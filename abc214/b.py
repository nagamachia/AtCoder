S,T = map(int,input().split())

ans=0

if T!=0:
    max_num=min(S,T)+1
else:
    max_num=S+1

for a in range(max_num):
    for b in range(max_num):
        for c in range(max_num):
            if a+b+c<=S and a*b*c<=T:
                ans+=1

print(ans)
S = int(input())
ans = 0

maxT = int(S/3)

res = S%3

if res==0:
    ans+=1
elif res==1:
    ans+=maxT
else:
    ans+=maxT+int(maxT*(maxT-1)*0.5)

for t in range(maxT-1,0,-1):
    exit()
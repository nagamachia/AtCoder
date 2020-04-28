li = list(map(int,input().split()))
ans=li[2]-(li[0]-li[1])
if ans>=0:
    print(ans)
else:
    print("0")

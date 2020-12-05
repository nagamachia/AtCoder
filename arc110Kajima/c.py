import math

N = int(input())
P = list(map(int,input().split()))

histry = [0]*(N-1)
ans = []

arr = P
count = 0
# maxi=N-1
# maxj=N-1
for i in range(N):
# i=0
# while i<=maxi:
    # 3. 走査範囲を前からひとつ狭める
    flag=0
    for j in reversed(range(i+1, N)):
    # j=maxj
    # while j>=i+1:
        # 1. 後ろから順に隣り合う要素を比較する。
        if arr[j-1] > arr[j]:
            # 2. 左が右の要素に比べ大きい場合交換する。
            if histry[j-1]!=0:
                print(-1)
                exit()
            count+=1
            histry[j-1]=count
            ans.append(j)
            arr[j-1], arr[j] = arr[j], arr[j-1]
            flag+=1
            # if flag==1:
            #     maxj=j-1
            #     maxi=j-2
        # j-=1
    # i+=1
    if flag==0:
        break

if 0 in histry:
    print(-1)
    exit()

for i in ans:
    print(i)
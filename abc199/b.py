N=int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

mx=1000
mn=1

# for i in range(N):
#     mx=min(B[i],mx)
#     mn=max(A[i],mn)

mx=min(B)
mn=max(A)

ans = mx-mn+1
if ans<0:
    print(0)
else:
    print(ans)
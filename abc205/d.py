N,Q = map(int,input().split())
A = list(map(int,input().split()))

K=[0]*Q

for q in range(Q):
    K[q]=int(input())

A=[0]+A
C=[0]*(N+1)

for i in range(1,N+1):
    C[i]=C[i-1]+A[i]-A[i-1]-1


for k in K:
    low=1
    high=N
    if C[N]<k:
        ans=A[N]+k-C[N]
    else:
        while low < high:
            mid = (low+high)//2
            if C[mid]>=k:
                high=mid
            else:
                low=mid+1
        ans=A[low]-1-C[low]+k
    print(ans)

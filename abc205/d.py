N,Q = map(int,input().split())
A = list(map(int,input().split()))

K=[0]*Q

for q in range(Q):
    K[q]=int(input())

maxK = max(K)
ans = [0]*maxK
start=1
startidx=0
cnt=0

while ans[-1]==0:
    # print(ans)
    if cnt<N:
        minA=A[cnt]
        if start!=minA:
            if startidx+minA-start<=maxK:
                ans[startidx:startidx+minA-start]=list(range(start,minA))
            else:
                ans[startidx:]=list(range(start,start+maxK-startidx))
        # for n in range(start,min(A)):
        #     ans[startidx] = n
        #     startidx+=1
        startidx+=minA-start
        start=minA+1
        cnt+=1
    else:
        ans[startidx:]=list(range(A[-1]+1,maxK-startidx+A[-1]+1))

# print(ans)

for k in K:
    print(ans[k-1])
    

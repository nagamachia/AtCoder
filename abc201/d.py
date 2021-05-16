H,W = map(int,input().split())

A = [input() for _ in range(H)]

d = {'+':1, '-':-1}

dp = [[0]*W for _ in range(H)]

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if i==H-1 and j==W-1:
            continue

        if (i+j)%2==0:
            dp[i][j] = -(10**10)
            if i+1<H:
                dp[i][j]=max(dp[i][j], dp[i+1][j]+d[A[i+1][j]])
            if j+1<W:
                dp[i][j]=max(dp[i][j], dp[i][j+1]+d[A[i][j+1]])
        else:
            dp[i][j] = 10**10
            if i+1<H:
                dp[i][j]=min(dp[i][j], dp[i+1][j]-d[A[i+1][j]])
            if j+1<W:
                dp[i][j]=min(dp[i][j], dp[i][j+1]-d[A[i][j+1]])

        # if i+1<H:
        #     dp[i][j]=max(dp[i][j], -dp[i+1][j]+d[A[i+1][j]])
        # if j+1<W:
        #     dp[i][j]=max(dp[i][j], -dp[i][j+1]+d[A[i][j+1]])


if dp[0][0]>0:
    print("Takahashi")
elif dp[0][0]==0:
    print("Draw")
else:
    print("Aoki")
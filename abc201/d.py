H,W = map(int,input().split())

A = ['']*H

for i in range(H):
    A[i] = input()

t = 0
a = 0

for h in range(H):
    for w in range(W):
        if (h+w)%2==1:
            if A[h][w]=='+':
                t+=1
            else:
                t-=1
        else:
            if A[h][w]=='+':
                a+=1
            else:
                a-=1            

if A[0][0]=='+':
    a-=1
else:
    a+=1

if t>a:
    print("Takahashi")
elif t==a:
    print("Draw")
else:
    print("Aoki")
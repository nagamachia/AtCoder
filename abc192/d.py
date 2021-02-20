import math

X = input()
M = int(input())

n = len(X)

if n==1:
    if M >= int(X):
        print(1)
    else:
        print(0)
    exit()

x = int(max(X))
y = 10**18+1
while x < y:
    z = (x+y)//2
    if M >= sum(int(X[n-i-1]) * z ** i for i in range(n)):
        x = z+1
    else:
        y=z


print(max(0,y-int(max(X))-1))

S = input()
Q = int(input())
Que = []
for i in range(Q):
    qi = input().split()
    if qi[0] == '1':
        S=S[::-1]
    elif qi[1] == '1':
        S = qi[2]+S
    else:
        S = S+qi[2]
print(S)

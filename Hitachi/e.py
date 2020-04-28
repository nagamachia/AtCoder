S = input()
Q = int(input())
for i in set(range(Q)):
    qi = input().split()
    if qi[0] == '1':
        S=''.join(list(reversed(S)))
        # S=S[::-1]
    elif qi[1] == '1':
        S = qi[2]+S
    else:
        S = S+qi[2]
print(S)

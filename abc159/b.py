S = input()
N = len(S)
S_inv = S[::-1]

if S == S_inv and S[:int((N-1)/2)] == S_inv[int((N+1)/2):] and S[int((N+1)/2):] == S_inv[:int((N-1)/2)]:
    print('Yes')
else:
    print('No')
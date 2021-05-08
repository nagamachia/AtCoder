# import numpy as np
N = int(input())
S = input()
Q = int(input())
TAB=[]
for q in range(Q):
    TAB.append(list(map(int,input().split())))

# -----------------------------
# Si = np.array(range(2*N))

# for q in range(Q):
#     if TAB[q][0]==1:
#         Si[TAB[q][1]-1],Si[TAB[q][2]-1] = Si[TAB[q][2]-1],Si[TAB[q][1]-1]
#     else:
#         Si[:N],Si[N:] = Si[N:],Si[:N].copy()

# s=list(S)
# for i in range(2*N):
#     s[i]=S[Si[i]]


# -------------------------------------
swpflag=False
def T1(s,A,B,swpflag):
    if swpflag:
        if A<N and B<N:
            s[A+N],s[B+N]=s[B+N],s[A+N]
        elif A<N and B>=N:
            s[A+N],s[B-N]=s[B-N],s[A+N]
        elif A>=N and B<N:
            s[A-N],s[B+N]=s[B+N],s[A-N]
        else:
            s[A-N],s[B-N]=s[B-N],s[A-N]
    else:
        s[A],s[B]=s[B],s[A]
    return s

s=list(S)

for q in range(Q):
    if TAB[q][0]==1:
        # s[TAB[q][1]-1],s[TAB[q][2]-1]=s[TAB[q][2]-1],s[TAB[q][1]-1]
        s = T1(s,TAB[q][1]-1,TAB[q][2]-1,swpflag)
    else:
        swpflag=not(swpflag)
        # s=s[N:]+s[:N]

if swpflag:
    s=s[N:]+s[:N]

ans = "".join(s)

print(ans)
import numpy as np

N=int(input())

S=[]
T=[]

for i in range(N):
    S.append(list(map(int,input().split())))
S=np.array(S)

for i in range(N):
    T.append(list(map(int,input().split())))
T=np.array(T)

Sm=np.mean(S,axis=0)
Tm=np.mean(T,axis=0)

Sv=S-Tm
Tv=T-Tm
# Sv=[]
# for i in range(N):
#     Sv.append([S[i][0]-Sm[0],S[i][1]-Sm[1]])

# Tv=[]
# for i in range(N):
#     Tv.append([T[i][0]-Tm[0],T[i][1]-Tm[1]])

if N==1:
    print("Yes")
    exit()

print(Sv,Tv)

Sod=[]
for i in range(1,N):
    Sod.append(Sv[0][0]*Sv[i][1]-Sv[0][1]*Sv[i][0])
Sod.sort()

Tod=[]
for i in range(1,N):
    Tod.append(Tv[0][0]*Tv[i][1]-Tv[0][1]*Tv[i][0])
Tod.sort()

if Sod==Tod:
    print("Yes")
else:
    print("No")
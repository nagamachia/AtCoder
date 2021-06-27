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

# print("S",S)
# print("T",T)

if N==1:
    print("Yes")
    exit()
elif N==2:
    if np.sum((S[0]-S[1])**2)==np.sum((T[0]-T[1])**2):
        print("Yes")
        exit()
    else:
        print("No")
        exit()

Sm=np.mean(S,axis=0)
Tm=np.mean(T,axis=0)

# print("Sm",Sm)
# print("Tm",Tm)

Sv=S-Sm
Tv=T-Tm

# Sn=np.sum(np.abs(Sv)**2,axis=-1)
# Tn=np.sum(np.abs(Tv)**2,axis=-1)

# Sv=Sv[np.where(Sn!=0)]
# Tv=Tv[np.where(Tn!=0)]

# print("Sv",Sv)
# print("Tv",Tv)

if len(Sv)!=len(Tv):
    print("No")
    exit()

Sp=[]
Tp=[]

for i in range(N):
    # if Sv[i][0]**2+Sv[i][1]**2>1e-10:
    Sp.append([Sv[i][0], Sv[i][1], round(Sv[i][0]**2+Sv[i][1]**2,11), round(np.arctan2(Sv[i][1],Sv[i][0]),11)])
    # if Tv[i][0]**2+Tv[i][1]**2>1e-10:
    Tp.append([Tv[i][0], Tv[i][1], round(Tv[i][0]**2+Tv[i][1]**2,11), round(np.arctan2(Tv[i][1],Tv[i][0]),11)])

# print("Sp",Sp)
# print("Tp",Tp)

Sp_sort = sorted(Sp, key=lambda x: (x[3],x[2]))
Tp_sort = sorted(Tp, key=lambda x: (x[3],x[2]))
# print("Sp_sort",Sp_sort)
# print("Tp_sort",Tp_sort)

if Sp_sort[0][2]<1e-10 and Tp_sort[0][2]<1e-10:
    Sp_sort=Sp_sort[1:]
    Tp_sort=Tp_sort[1:]
elif Sp_sort[0][2]<1e-10 or Tp_sort[0][2]<1e-10:
    print("No")
    exit()

Sdot=[]
Tdot=[]
for i in range(N-1):
    Sdot.append(Sp_sort[i][2])
    Sdot.append(round(Sp_sort[i][0]*Sp_sort[i+1][0]+Sp_sort[i][1]*Sp_sort[i+1][1],11))
    Sdot.append(round(Sp_sort[i][0]*Sp_sort[i+1][1]-Sp_sort[i][1]*Sp_sort[i+1][0],11))
    Tdot.append(Tp_sort[i][2])
    Tdot.append(round(Tp_sort[i][0]*Tp_sort[i+1][0]+Tp_sort[i][1]*Tp_sort[i+1][1],11))
    Tdot.append(round(Tp_sort[i][0]*Tp_sort[i+1][1]-Tp_sort[i][1]*Tp_sort[i+1][0],11))
Sdot.append(Sp_sort[N-1][2])
Sdot.append(round(Sp_sort[N-1][0]*Sp_sort[0][0]+Sp_sort[N-1][1]*Sp_sort[0][1],11))
Sdot.append(round(Sp_sort[N-1][0]*Sp_sort[0][1]-Sp_sort[N-1][1]*Sp_sort[0][0],11))
Tdot.append(Tp_sort[N-1][2])
Tdot.append(round(Tp_sort[N-1][0]*Tp_sort[0][0]+Tp_sort[N-1][1]*Tp_sort[0][1],11))
Tdot.append(round(Tp_sort[N-1][0]*Tp_sort[0][1]-Tp_sort[N-1][1]*Tp_sort[0][0],11))

for i in range(0,3*N,3):
    if Sdot==Tdot[i:]+Tdot[:i]:
        print("Yes")
        exit()

print("No")

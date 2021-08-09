N,M = map(int,input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

def bin_search(list, search_v):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_v = list[mid]

        if search_v == mid_v:
            return mid, 0
        if search_v < mid_v:
            if search_v > list[mid-1]:
                return mid-1
            high = mid - 1, 1
            continue
        if search_v > mid_v:
            if search_v < list[mid+1]:
                return mid, 1
            low = mid + 1
            continue
    return None

A=list(A).sorted()
B=list(B).sorted()

ans=10**10
# start=0

Amax=A[-1]
Amin=A[0]
Bmax=B[-1]
Bmin=B[0]

if Bmax <= Amin:
    ans=abs(Amin-Bmax)
elif Amax <= Bmin:
    ans=abs(Bmin-Amax)
elif Amax>=Bmax and Bmax>=Amin and Amin>=Bmin:
    start,snum = bin_search(B,Amin)
    end,enum = bin_search(A,Bmax)
    Astart=0
    for m in range(start,M):
        idx,inum = bin_search(A[Astart:end+enum],B[m])
        if inum==0:
            ans=0
            break
        Astart = idx
        ans=min([ans,abs(B[m]-A[idx]),abs[A[idx+1]-B[m]]])
elif Bmax>=Amax and Amax>=Bmin and Bmin>=Amin:
    start,snum = bin_search(A,Bmin)
    end,enum = bin_search(B,Amax)
    Bstart=0
    for n in range(start,N):
        idx,inum = bin_search(B[Bstart:end+enum],A[n])
        if inum==0:
            ans=0
            break
        Bstart = idx
        ans=min([ans,abs(A[n]-B[idx]),abs[B[idx+1]-A[n]]])
elif Amax>=Bmax and Bmin>=Amin:
    start,snum = bin_search(B,Amin)
    end,enum = bin_search(A,Bmax)
    Astart=0
    for m in range(start,M):
        idx,inum = bin_search(A[Astart:end+enum],B[m])
        if inum==0:
            ans=0
            break
        Astart = idx
        ans=min([ans,abs(B[m]-A[idx]),abs[A[idx+1]-B[m]]])


# for n in range(N):
#     for m in range(start,M):
#         d=abs(A[n]-B[m])
#         if m!=0:
#             if d>abs(A[n]-B[m-1]):
#                 start=m-1
#                 continue
#         ans=min(ans,d)

# print(ans)

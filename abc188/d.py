import numpy as np

N,C = map(int,input().split())
abc =[]
for i in range(N):
    abc.append(list(map(int,input().split())))

abc = np.array(abc)

start = min(abc[:,0])
end = max(abc[:,1])

# useDay = np.zeros((N,end-start+1),dtype=np.int)
noPrimeDay = np.zeros((end-start+1),dtype=np.int)

for i in range(N):
    noPrimeDay[abc[i][0]-1:abc[i][1]] += abc[i][2]
#     useDay[i][abc[i][0]-1:abc[i][1]] = abc[i][2]
noPrimeDay = np.clip(noPrimeDay,None,C)
# ans = 0
ans = np.sum(noPrimeDay)

# for j in range(end-start+1):
#     # ans += min(np.sum(useDay[:,j]), C)
#     ans += min(noPrimeDay[j],C)

print(int(ans))
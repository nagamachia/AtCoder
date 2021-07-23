# import numpy as np

N,K = map(int,input().split())

c = list(map(int,input().split()))

ans=len(set(c[:K]))
max_idx=[0]
for i in range(K,N-K+1,K):
    s=len(set(c[i:i+K]))
    if s>ans:
        max_idx=[i]
        ans=s
    elif s==ans:
        max_idx.append(i)

s=len(set(c[N-K:]))
if s>ans:
    max_idx=[N-K]
    ans=s
elif s==ans:
    max_idx.append(N-K)

r=[]
for i in max_idx:
    r+=list(range(max(i-K+1,0),min(i+K-1,N-K+1)))
r=set(r)

for i in max_idx:
    r.discard(i)

# for i in max_idx:
#     for j in range(max(i-K+1,0),min(i+K-1,N-K+1)):
for j in r:
    if j==i:
        continue
    ans=max(ans,len(set(c[j:j+K])))

print(ans)
# ans=len(set(c[:K]))
# is_right=True
# max_idx=0

# for i in range(1,N-K+1):
#     # print("max_idx:",max_idx)
#     if is_right:
#         # print(c[i:i+K])
#         if c[i] in c[i+1:i+K]:
#             max_idx=i
#         else:
#             max_idx=i
#             is_right=False
#     else:
#         if len(set(c[i:i+K])) >= len(set(c[max_idx:max_idx+K])):
#             max_idx=i
#             is_right=True

# print(len(set(c[max_idx:max_idx+K])))
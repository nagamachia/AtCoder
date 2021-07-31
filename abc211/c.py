from collections import Counter

S=input()

# S=list(S)
# c=Counter(list(S))

# print(c)
mod = 10**9+7

# ans = c['c']%mod*c['h']%mod*c['o']%mod*c['k']%mod*c['u']%mod*c['d']%mod*c['a']%mod*c['i']%mod
chokudai='chokudai'

chok_dic={}
for c in chokudai:
    chok_dic[c]=[]

for n,v in enumerate(S):
    if v in chokudai:
        chok_dic[v].append(n)

chok_dic['c']

for c in chokudai[1:]:
    chok_dic[c]

print(ans)
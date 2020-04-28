K = int(input())
i = 9
ans = [1,2,3,4,5,6,7,8,9]

while len(ans) >= K:
    i += 1
    si = str(i)
    res = []
    for j in range((len(si)-1)):
        res.append(abs(int(si[j])-int(si[j+1])))
    if all([i <= 1 for i in res]):
        ans.append(i)

print(ans[K-1])
"""
lunlun = ['0','1','2','3','4','5','6','7','8','9']
lun = ['0','1','2','3','4','5','6','7','8','9']

while len(ans) >= K:
    for i in lun:
        
    # for i in range(1,9):
    #     ll = int(str(i)*2)
    # lun.append([ll-1,ll,ll+1])
"""
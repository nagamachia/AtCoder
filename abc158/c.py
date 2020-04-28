import math
A,B = map(int, input().split())

mn = max(A/0.08,10*B)
mni = math.ceil(mn)
mx = min((A+1)/0.08,10*(B+1))
mxi = int(mx)
# print(A/0.08,(A+1)/0.08)
# print(10*B,10*(B+1))
# print(minans,maxans)
if mn <= mx and (mxi>mn and mx>mni):
    print(mni)
else:
    print(-1)
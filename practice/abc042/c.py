import numpy as np

N,K = input().split()
D = list(map(int, input().split()))

num = [0,1,2,3,4,5,6,7,8,9]

for d in D:
    num.remove(d)

# print(num)

ans = ""
flag = 0

for n in N:
    gt = [nu for nu in num if nu > int(n)]
    if flag == 0:
        if gt != []:
            ans += str(min(gt))
            flag = 1
        elif n in num:
            ans += str(min(n))
        else:
            pass
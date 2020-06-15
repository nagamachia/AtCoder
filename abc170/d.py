import numpy as np

N = int(input())
A = list(map(int, input().split()))
# A = np.array(A)
# def div(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]

ans = 0

for i in range(N):
    Ao = np.array(A[:i]+A[i+1:])
    Ao = Ao[Ao<=A[i]]
    # mod = set(A) & set(div(A[i]))
    # print(div(a))

    if all([A[i]%a!=0 for a in Ao]):
    # if len(mod)==1:
        ans+=1

print(ans)

import math
import numpy as np
H,N = map(int, input().split())
A = np.zeros(N)
B = np.zeros(N)
rate = np.zeros(N)
for i in range(N):
    A_,B_ = map(int, input().split())
    A[i] = A_
    B[i] = B_
    rate[i] = A_/B_
if A[A >= H]:

print(rate)

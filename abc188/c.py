import numpy as np

N = int(input())
A = np.array(list(map(int,input().split())))

# print(np.argmax(A[:2**(N-1)]))
# print(np.argmax(A[2**(N-1):]))
l = np.argmax(A[:2**(N-1)])
r = np.argmax(A[2**(N-1):])
if A[l]>A[2**(N-1)+r]:
    print(2**(N-1)+r+1)
else:
    print(l+1)
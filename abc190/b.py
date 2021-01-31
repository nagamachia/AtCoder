# import numpy as np

N,S,D = map(int,input().split())
XY = []

for i in range(N):
    XY.append(list(map(int,input().split())))

for i in range(N):
    if XY[i][0]<S and XY[i][1]>D:
        print("Yes")
        exit()
print("No")
# XY = np.array(XY)

# print(np.any(XY[0]<S and XY[1]>D))
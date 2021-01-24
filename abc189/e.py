import numpy as np

def op1(xy):
    xy_op = xy.copy()
    xy_op[0] = xy[1]
    xy_op[1] = -xy[0]
    return xy_op

def op2(xy):
    xy_op = xy.copy()
    xy_op[0] = -xy[1]
    xy_op[1] = xy[0]
    return xy_op

def op3(xy,p):
    xy_op = xy.copy()
    xy_op[1] = 2*p-xy[1]
    return xy_op

def op4(xy,p):
    xy_op = xy.copy()
    xy_op[0] = 2*p-xy[0]
    return xy_op

N = int(input())
for i in range(N):
    XY.append(list(map(int,input().split())))
XY = np.array(XY)

M = int(input())
op = []
for i in range(M):
    op.append(input())

Q = int(input())
AB = []
for i in range(Q):
    AB.append(list(map(int,input().split())))
AB = np.array(AB)

uqB = np.unique(AB[:,1])

ans = []

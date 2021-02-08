from math import floor,ceil
from decimal import Decimal

X,Y,R = map(Decimal,input().split())

rate = 10000
irate = 0.0001

minx = ceil(X-R)*rate
halfx = floor(X)*rate
maxx = floor(X+R)*rate

miny = ceil(Y-R)*rate
maxy = floor(Y+R)*rate

tmpminy = ceil(Y-R)*rate
tmpmaxy = floor(Y+R)*rate

ans = 0

X=round(X*rate)
Y=round(Y*rate)
R=round(R*rate)

for i in range(halfx,minx-rate,-rate):
    minflag=0
    maxflag=0
    for j in range(miny,maxy+rate,rate):
        if (i-X)**2+(j-Y)**2<=R**2:
            # minj=j
            miny=j
            minflag=1
            break
    for j in range(maxy,miny-rate,-rate):
        if (i-X)**2+(j-Y)**2<=R**2:
            # maxj=j
            maxy=j
            maxflag=1
            break
    if minflag and maxflag:
        ans += int((maxy-miny)*irate)+1

miny = tmpminy
maxy = tmpmaxy
for i in range(halfx+rate,maxx+rate,rate):
    for j in range(miny,maxy+rate,rate):
        if (i-X)**2+(j-Y)**2<=R**2:
            # minj=j
            miny=j
            break
    for j in range(maxy,miny-rate,-rate):
        if (i-X)**2+(j-Y)**2<=R**2:
            # maxj=j
            maxy=j
            break
    
    ans += int((maxy-miny)*irate)+1

print(ans)

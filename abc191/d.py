import math

X,Y,R = map(float,input().split())

rate = 10000
irate = 0.0001

minx = math.ceil(X-R)*rate
halfx = int(X)*rate
maxx = int(X+R)*rate

miny = math.ceil(Y-R)*rate
maxy = int(Y+R)*rate

tmpminy = math.ceil(Y-R)*rate
tmpmaxy = int(Y+R)*rate

ans = 0

X=int(X*rate)
Y=int(Y*rate)
R=int(R*rate)

for i in range(halfx,minx-rate,-rate):
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

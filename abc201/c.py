S = input()

o=0
x=0
q=0

for i in range(10):
    if S[i]=="o":
        o+=1
    elif S[i]=="x":
        x+=1
    else:
        q+=1

if o>4 or x==10:
    print(0)
else:
    if o==0:
        ans = q**4
    elif o==1:
        ans = (o+q)**4-q**4
    elif o==2:
        ans = 4*2+6+2*6*2*q+12*q**2
    elif o==3:
        ans = 3*6*2+24*q
    else:
        ans = 24
    print(ans)
    



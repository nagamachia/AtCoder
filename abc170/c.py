X,N = map(int, input().split())
p = list(map(int, input().split()))

i = 0

while X+i<=101 or X-i>=0:
    pflag = X+i in p
    mflag = X-i in p
    if pflag and mflag:
        i+=1
    else:
        if not mflag:
            print(X-i)
            exit()
        else:
            print(X+i)
            exit()

# if 101-X <= X:
#     print(0)
# else:
#     print(101)

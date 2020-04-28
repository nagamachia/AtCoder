A,B,C=map(int,input().split())
if A==B or A==C or B==C:
    if A==B and A==C:
        print('No')
    else:
        print('Yes')
else:
    print('No')

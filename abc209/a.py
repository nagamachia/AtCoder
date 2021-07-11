A,B=map(int,input().split())

dst=B-A

if dst>=0:
    print(B-A+1)
else:
    print(0)
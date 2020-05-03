K = int(input())
A,B = map(int, input().split())

if A%K == 0:
    print("OK")
elif K*(int(A/K)+1) <= B:
    print("OK")
else:
    print("NG")
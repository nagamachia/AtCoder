N = int(input())

# S = []

TC = ['AC','WA','TLE','RE']
C = [0,0,0,0]

for i in range(N):
    # S.append(input())
    result = input()
    if result==TC[0]:
        C[0]+=1
    elif result==TC[1]:
        C[1]+=1
    elif result==TC[2]:
        C[2]+=1
    else:
        C[3]+=1

print("AC x "+str(C[0]))
print("WA x "+str(C[1]))
print("TLE x "+str(C[2]))
print("RE x "+str(C[3]))


N=input()

if N=='0':
    print("Yes")
    exit()

for i in range(len(N)):
    if N[i]!='0':
        l=i
        break

for i in reversed(range(len(N))):
    if N[i]!='0':
        r=i
        break

N0=N[l:r+1]

if N0==N0[::-1]:
    print("Yes")
else:
    print("No")
S = input()
ans = 0
# print(len(S))
lS = len(S)

if int(S) < 2019:
     ans = 0
else:
     for i in range(lS-3):
          for j in range(lS-3-i):
               obj = S[j:j+4+i]
               if int(obj)%2019==0:
                    ans+=1

print(ans)
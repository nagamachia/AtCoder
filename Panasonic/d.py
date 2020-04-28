N = int(input())

ans=[]
abc=[1,12,123,1234,12345,123456,1234567,12345678,123456789]

b = int('1'*(N-1),2)

for i in range(b+1):
    ans.append('0'+format(i,'0'+str(N-1)+'b'))
ans0=int(ans[-1])
for j in range(1,abc[N-3]+1):
    ans.append('0'+str(ans0+j))

print(ans)
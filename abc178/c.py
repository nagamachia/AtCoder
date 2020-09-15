N = int(input())
mod = pow(10,9)+7

if N==1:
    ans = 0
else:
    ans = pow(10,N,mod)+pow(8,N,mod)-pow(9,N,mod)-pow(9,N,mod)

print(ans%mod)
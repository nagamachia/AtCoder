import time
start = time.time()
def main():
  n,a,b = map(int,input().split())
  MOD = 10 ** 9 + 7
  ans = pow(2,n,MOD) - 1
  P = 1
  F = 1
 
  for i in range(1,b + 1):
    P = P * (n - i + 1) % MOD #P!
    F = F * i % MOD  # i! 
    if i == a or i == b:
      #Fの逆元のmodをとる
      ans -= P * pow(F,MOD - 2,MOD)
  
  print(ans % MOD)
 
main()
end = time.time()
print (end-start)
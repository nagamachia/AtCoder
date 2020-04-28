N,K = map(int, input().split())
mod = 10**9+7
ans = (((2*K-1)*(K-1)%mod*K%mod - (2*N+3)*(N+2)%mod*(N+1)%mod \
     + 3*(N+1)*(N+1)%mod*(N+2)%mod - 3*(N+1)*K%mod*(K-1)%mod)*pow(6,mod-2,mod) \
     + (N-K+2))%mod
# ans = (((2*K-1)*(K-1)%mod*K%mod - (2*N+3)*(N+2)%mod*(N+1)%mod \
#      + 3*(N+1)*(N+1)%mod*(N+2)%mod - 3*(N+1)*K%mod*(K-1)%mod)/6 \
#      + (N-K+2))%mod

print(int(ans))
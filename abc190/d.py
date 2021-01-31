N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

div = make_divisors(2*N)
ans=0

for n in div:
    if (2*N/n-n+1)%2==0:
        ans+=1

print(ans)

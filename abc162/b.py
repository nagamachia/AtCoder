N = int(input())

ans = N*(N+1)*0.5

fizz = int(N/3)
buzz = int(N/5)
fizzbuzz = int(N/15)

fizzsum = 3*0.5*fizz*(fizz+1)
buzzsum = 5*0.5*buzz*(buzz+1)
fizzbuzzsum = 15*0.5*fizzbuzz*(fizzbuzz+1)

ans = ans - fizzsum - buzzsum + fizzbuzzsum

print(int(ans))
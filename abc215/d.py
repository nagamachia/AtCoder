N,M = map(int,input().split())

A = list(map(int,input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr

divs = []

for a in A:
    divs = divs + factorization(a)

divs = set(divs)
divs.remove(1)

ans = [1]

# for m in range(2,M+1):
#     if divs & set(make_divisors(m)) == set():
#         ans.append(m)

targets = list(range(M+1))

print(divs)

for d in divs:
    targets = [t for t in targets if t%d!=0]

# while targets!=[]:
#     m = targets[0]
#     if divs & set(factorization(m)) == set():
#         ans.append(m)
#         targets.remove(m)
#     else:
#         targets = [t for t in targets if t%m!=0]

print(len(targets))
for a in targets:
    print(a)


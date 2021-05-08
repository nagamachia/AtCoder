N = int(input())
# A = input().split()
A = [s.zfill(2) for s in input().split()]

ans=0

end2=set([s[len(s)-2:] for s in A])



for i in end2:
    l100 = [s[:len(s)-2] for s in A if s.endswith(i)]
    n2=0
    if len(l100)>=2:
        for l in l100:
            if l=='':
                l='0'
            if int(l)%2==0:
                n2+=1
        n1=len(l100)-n2
        ans+=int((n2*(n2-1)+n1*(n1-1))*0.5)
    A = [s for s in A if not s.endswith(i)]

print(ans)


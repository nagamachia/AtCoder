A,B,C=map(int,input().split())

def compare(A,B):
    if A>B:
        ans = ">"
    elif A==B:
        ans = "="
    else:
        ans = "<"
    return ans


if C%2==0:
    ans = compare(abs(A),abs(B))
else:
    if A>=0 and B<0:
        ans = ">"
    elif A<0 and B>=0:
        ans = "<"
    elif A<0 and B<0:
        ans = compare(abs(B),abs(A))
    else:
        ans = compare(A,B)

print(ans)


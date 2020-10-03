import re

N,S = input().split()
N = int(N)

def is_complement(s):
    
    num = s.count('X')
    s.replace('X','')

    # a = re.findall('A',s)
    # t = re.findall('T',s)
    # c = re.findall('C',s)
    # g = re.findall('G',s)
    a = s.count('A')
    t = s.count('T')
    c = s.count('C')
    g = s.count('G')

    num += (min(a,t)+min(c,g))*2

    answer = False

    if len(s)==num:
        answer = True

    return answer

ans = 0

for i in range(2,N+1,2):
    for j in range(N-i+1):
        JI=[]
        # print(i,j)
        # print(S[j:j+i])
        if is_complement(S[j:j+i]):
            JI.append([j,i])
            ans += 1
    for ji in JI:
        S = S[:ji[0]]+'X'*ji[1]+S[ji[0]+ji[1]:]

print(ans)
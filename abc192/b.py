import re

S = input()

Sodd = S[::2]
Seven = S[1::2]

if len(S)==1:
    if re.fullmatch(r'[a-z]',Sodd):
        print('Yes')
    else:
        print("No")
elif re.fullmatch(r'[a-z]+',Sodd) and re.fullmatch(r'[A-Z]+',Seven):
    print("Yes")
else:
    print("No")
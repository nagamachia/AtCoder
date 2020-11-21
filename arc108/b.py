import re

N = int(input())
s = input()

# F = re.findall('[fox]+', s)
# F = re.findall('[fox]+', s)
# fox = 'fox'

# res = N - len(''.join(F))

# for i in range(len(F)):
#     while fox in F[i]:
#         # F[i] = F[i].replace('ffffoxoxoxox','')
#         # F[i] = F[i].replace('fofffoxoxoxx','')
#         # F[i] = F[i].replace('ffoffoxoxxox','')
#         # F[i] = F[i].replace('fofoffoxoxxx','')
#         # F[i] = F[i].replace('fffofoxxoxox','')
#         # F[i] = F[i].replace('foffofoxxoxx','')
#         # F[i] = F[i].replace('ffofofoxxxox','')
#         # F[i] = F[i].replace('fofofofoxxxx','')
#         # F[i] = F[i].replace('fffoxoxox','')
#         # F[i] = F[i].replace('foffoxoxx','')
#         # F[i] = F[i].replace('ffofoxxox','')
#         # F[i] = F[i].replace('fofofoxxx','')
#         # while 'ffoxox' in F[i] or 'fofoxx' in F[i]:
#         #     F[i] = F[i].replace('ffoxox','')
#         #     F[i] = F[i].replace('fofoxx','')
#         F[i] = F[i].replace(fox,'')

# ans = res + len(''.join(F))

while 'fox' in s:
    s = s.replace('fox','')

ans = len(s)

print(ans)
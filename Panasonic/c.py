from math import sqrt
from decimal import Decimal
# def sqrt2(n):
#     def f(prev):
#         while True:
#             m = (prev + n / prev) / 2
#             if m >= prev:
#                 return prev
#             prev = m
    
#     return f(math.sqrt(n) * (1 + 1e-10))
a,b,c = map(int, input().split())

# ra = math.sqrt(a)
# rb = math.sqrt(b)
# rc = math.sqrt(c)
ra = Decimal(a).sqrt()
rb = Decimal(b).sqrt()
rc = Decimal(c).sqrt()

if rc > ra + rb:
    print('Yes')
else:
    print('No')

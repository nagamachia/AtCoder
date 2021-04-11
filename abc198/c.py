# import math
from decimal import Decimal,ROUND_CEILING,getcontext,ROUND_FLOOR

R,X,Y = map(int,input().split())

# getcontext().prec = 28
# ans = math.ceil(math.sqrt(X**2+Y**2)/R)

# ans2 = Decimal(str(X**2+Y**2)).sqrt()/Decimal(str(R))
ans2 = Decimal(str(X**2+Y**2))/Decimal(str(R**2))
# ans = math.ceil(math.sqrt(ans2))
# ans = int(ans2.quantize(Decimal('1.'), rounding=ROUND_CEILING))
ans = int(ans2.sqrt().quantize(Decimal('1.'), rounding=ROUND_CEILING))

if R**2>X**2+Y**2:
    print(2)
else:
    print(ans)
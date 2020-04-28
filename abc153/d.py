import math
import numpy as np
H=int(input())

n = int(np.log2(H))
ans = 2**(n+1)-1
print(ans)

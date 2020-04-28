import math
import numpy as np
a=int(input())
l=(np.arange(a)+1).tolist()
#print(l)
l_odd = [i for i in l if int(math.log10(i)) % 2 == 0]
#print(l_odd)
print(len(l_odd))

# floor-ceil-and-rint

import numpy as np
np.set_printoptions(legacy = "1.13")

arr = list(map(float, input().split()))
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
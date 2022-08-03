# np-shape-reshape

import numpy as np

arr = list(map(int, input().split()))
np_arr = np.array(arr).reshape(3,3)
print(np_arr)
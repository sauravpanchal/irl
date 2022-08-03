# np-inner-and-outer

import numpy as np

arr_a = np.array(list(map(int, input().split())))
arr_b = np.array(list(map(int, input().split())))

print(np.inner(arr_a, arr_b))
print(np.outer(arr_a, arr_b))
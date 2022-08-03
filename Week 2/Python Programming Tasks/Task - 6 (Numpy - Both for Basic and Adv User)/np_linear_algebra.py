# np-linear-algebra

import numpy as np

arr = list()
N = int(input())
for n in range(N):
    arr.append(list(map(float, input().split())))

arr = np.array(arr)
print(round(np.linalg.det(arr), 2))
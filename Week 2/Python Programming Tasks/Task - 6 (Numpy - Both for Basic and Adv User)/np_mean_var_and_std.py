# np-mean-var-and-std

import numpy as np

inp = input().split()
N, M = int(inp[0]), int(inp[1])

arr = list()
for n in range(N):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr, axis = None), 11))
# np-transpose-and-flatten

import numpy as np

inp = input().split()
N, M = int(inp[0]), int(inp[1])
arr = list()
for n in range(N):
    row_n = list(map(int, input().split()))
    arr.append(row_n)
arr = np.array(arr)
print(arr.T)
print(arr.flatten())
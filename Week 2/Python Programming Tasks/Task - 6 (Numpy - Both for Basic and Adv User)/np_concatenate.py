# np-concatenate

import numpy as np

inp = input().split()
N,M,P = int(inp[0]), int(inp[1]), int(inp[2])
arr = list()
for row in range(N+M):
    arr.append(input().split())
print(np.array(arr, dtype = int))
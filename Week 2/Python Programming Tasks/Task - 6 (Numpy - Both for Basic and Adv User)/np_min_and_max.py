# np-min-and-max

import numpy as np

inp = input().split()
N, M = int(inp[0]), int(inp[1])

arr = list()
for n in range(N):
    arr.append(list(map(int, input().split())))
    
print(np.max(np.min(arr, axis = 1)))
# np-sum-and-prod

import numpy as np

inp = input().split()
N, M = int(inp[0]), int(inp[1])

arr = list()
for n in range(N):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
print(np.prod(arr.sum(axis = 0)))
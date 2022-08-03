# np-eye-and-identity

import numpy as np
np.set_printoptions(legacy="1.13")

inp = input().split()
N, P = int(inp[0]), int(inp[1])
print(np.eye(N, P))
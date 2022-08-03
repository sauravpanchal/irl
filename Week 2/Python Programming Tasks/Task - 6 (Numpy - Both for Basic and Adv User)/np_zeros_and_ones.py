# np-zeros-and-ones

import numpy as np

# causes runtime error
# inp = input().split()
# N,P,Q = int(inp[0]), int(inp[1]), int(inp[2])
# print(np.zeros((N,P,Q), dtype = np.int))
# print(np.ones((N,P,Q), dtype = np.int))

# while passing size of numpy as tuple does the work
inp = tuple(map(int, input().split()))
print(np.zeros(inp, dtype = np.int))
print(np.ones(inp, dtype = np.int))
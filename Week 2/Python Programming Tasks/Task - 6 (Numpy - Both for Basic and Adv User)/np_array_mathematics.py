# np-array-mathematics

import numpy as np

inp = input().split()
N, M = int(inp[0]), int(inp[1])

# For A
arr_a = list() 
for n in range(N):
    arr_a.append(list(map(int, input().split())))

# For B
arr_b = list() 
for n in range(N):
    arr_b.append(list(map(int, input().split())))

# Taking input in this format created error
# arr_a = np.array([list(map(int, input().split()))])
# arr_b = np.array([list(map(int, input().split()))])

arr_a = np.array(arr_a)
arr_b = np.array(arr_b)

print(np.add(arr_a, arr_b))
print(np.subtract(arr_a, arr_b))
print(np.multiply(arr_a, arr_b))
print(arr_a // arr_b)
print(np.mod(arr_a, arr_b))
print(np.power(arr_a, arr_b))
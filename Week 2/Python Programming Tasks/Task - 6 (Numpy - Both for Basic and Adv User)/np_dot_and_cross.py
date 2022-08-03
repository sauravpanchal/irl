# np-dot-and-cross

import numpy as np

N = int(input())

arr_a = list()
for n in range(N):
    arr_a.append(list(map(int, input().split())))
arr_a = np.array(arr_a)

arr_b = list()
for n in range(N):
    arr_b.append(list(map(int, input().split())))    
arr_b = np.array(arr_b)
    
print(np.dot(arr_a, arr_b))
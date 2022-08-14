# s10-normal-distribution-1

import math

def cdf_func(mean, std, x):
    return  0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

mean, std = list(map(float, input().split(' ')))
exact = float(input().strip())
low, high = list(map(float, input().split(' ')))

print(round(cdf_func(mean, std, exact), 3))
print(round(cdf_func(mean, std, high) - cdf_func(mean, std, low), 3))
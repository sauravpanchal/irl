# s10-normal-distribution-2

import math

def cdf_func(mean, std, x):
    return  0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

mean, std = list(map(float, input().split(' ')))
high_score = float(input().strip())
passing_score = float(input().strip())

print(round((1 - cdf_func(mean, std, high_score)) * 100, 2))
print(round((1 - cdf_func(mean, std, passing_score)) * 100, 2))
print(round((cdf_func(mean, std, passing_score)) * 100, 2))
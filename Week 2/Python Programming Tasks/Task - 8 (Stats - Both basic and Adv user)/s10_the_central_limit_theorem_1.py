# s10-the-central-limit-theorem-1

import math

x = int(input())
n = int(input())
mean = int(input())
std = int(input())

mean_sum = n * mean 
std_sum = math.sqrt(n) * std

def cdf_func(x, mean, std):
    return 0.5*(1 + math.erf(((x - mean)/std)/(math.sqrt(2))))

print(round(cdf_func(x, mean_sum, std_sum), 4))
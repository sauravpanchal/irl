# s10-pearson-correlation-coefficient

from statistics import mean, pstdev

size = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean_X, mean_Y = mean(X), mean(Y)
std_X, std_Y = pstdev(X), pstdev(Y)

cov = sum([(X[i] - mean_X) * (Y[i] - mean_Y) for i in range(size)]) / size
pearson_coef = cov / (std_X * std_Y)

print(round(pearson_coef, 3))
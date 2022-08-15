# s10-least-square-regression-line

# hard-coded input was allowed
X = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n = 5
sigma_xi = sum(X)
x_bar = sigma_xi / n
sigma_yi = sum(y)
y_bar = sigma_yi / n
sigma_xi_square = sum([i ** 2 for i in X])
sigma_xy = sum([i * j for i, j in zip(X, y)])

numerator = (n * sigma_xy) - (sigma_xi * sigma_yi)
denominator = (n * sigma_xi_square) - (sigma_xi ** 2)
b = numerator / denominator
a = y_bar - (b * x_bar)

predict_for_x = 80
print(round(a + (b * predict_for_x), 3))
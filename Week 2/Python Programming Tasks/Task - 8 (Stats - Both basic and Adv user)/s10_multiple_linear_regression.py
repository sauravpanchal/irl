# s10-multiple-linear-regression

import numpy as np

def mlr(X, y, pred_X):
    transpose_X = X.T
    X = transpose_X.dot(X)
    inv_X = np.linalg.inv(X)
    product_of_inv_X_and_transpose_X = inv_X.dot(transpose_X)
    B = product_of_inv_X_and_transpose_X.dot(y)
    pred_y = pred_X.dot(B)
    
    return pred_y
    
m, n = map(int, input().split())
X = list()
y = list()
pred_X = list()

for i in range(n):
    *features, y_value = map(float, input().split())
    X.append([1] + features)
    y.append(y_value)

pred_total = int(input())
for i in range(pred_total):
    features = list(map(float, input().split()))
    pred_X.append([1] + features)
    
pred_y = mlr(np.array(X), np.array(y), np.array(pred_X))
for row in pred_y:
    print(round(row, 2))
# np-polynomials

import numpy as np

coef_ = list(map(float, input().split()))
x = int(input())
print(np.polyval(coef_, x))
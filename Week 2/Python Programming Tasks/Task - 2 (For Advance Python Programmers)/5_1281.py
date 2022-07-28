# subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        n = str(n)
        for i in n:
            product *= int(i)
            sum += int(i)
        return (product - sum)
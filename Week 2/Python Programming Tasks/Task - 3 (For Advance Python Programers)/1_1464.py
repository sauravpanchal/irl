# maximum-product-of-two-elements-in-an-array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        for i in range(len(nums)):
            for j in range(i): # for j in range(len(nums)) # gives wrong answer
                temp = (nums[i]-1) * (nums[j]-1)
                if temp >= max_product:
                    max_product = temp
        return max_product
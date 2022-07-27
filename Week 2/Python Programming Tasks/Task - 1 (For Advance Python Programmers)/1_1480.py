# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         sum_list = list()
#         for i in range(len(nums)):
#             sum_list.append(sum(nums[0:i+1]))
#         return sum_list
        return [sum(nums[0:i+1]) for i in range(len(nums))]
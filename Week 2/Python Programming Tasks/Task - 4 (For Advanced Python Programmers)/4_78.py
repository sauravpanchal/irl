# subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                result.append([num] + result[i])
                # print(result,[num],result[i]) # keep adding previous ones
        return result
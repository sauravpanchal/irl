# how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictionary = dict()
        result = list()
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dictionary:
                dictionary[sorted_nums[i]] = i
        for i in range(len(nums)):
            result.append(dictionary[nums[i]])
        return result
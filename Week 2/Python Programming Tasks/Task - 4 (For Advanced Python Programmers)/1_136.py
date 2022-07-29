# single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1
        for key,value in hash_map.items():
            if value == 1:
                return key
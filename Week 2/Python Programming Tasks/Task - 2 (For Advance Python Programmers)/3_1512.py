# number-of-good-pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        result = 0
        for i in nums:
            if i in d:
                if d[i] == 1:
                    result += 1
                else:
                    result += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return result
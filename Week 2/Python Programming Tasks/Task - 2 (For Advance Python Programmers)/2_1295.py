# find-numbers-with-even-number-of-digits/submissions/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count = 0
        # for i in nums:
        #     if len(str(i)) % 2 == 0:
        #         count += 1
        # return count
        return sum([1 if len(str(i)) % 2 == 0 else 0 for i in nums])
# Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = list()
        for i in range(n):
            l.extend([nums[i], nums[i+n]])
        return l
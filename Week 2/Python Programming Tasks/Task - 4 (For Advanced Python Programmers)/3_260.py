# single-number-iii

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        set_of_nums = set(nums)
        xor = 0
        for num in nums:
            xor = xor^num
        result = 0
        for num in nums:
            # num1 ^ num2 = num3 => num1 ^ num3 = num2 => num2 ^ num3 => num1
            if num ^ xor in set_of_nums:
                result = [num, xor ^ num]
        return result
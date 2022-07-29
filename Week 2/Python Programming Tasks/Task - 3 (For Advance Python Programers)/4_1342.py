# number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        for n in range(num):
            if num == 0:
                break
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            count += 1
        return count
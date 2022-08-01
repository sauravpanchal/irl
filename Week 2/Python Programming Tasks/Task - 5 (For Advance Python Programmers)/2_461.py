# hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        xor = x^y
        while xor > 0: # xor will become 0 when there's not difference between 2 numbers, hence hammign distance will be 0 which is when we exit the while loop
            xor &= xor-1
            hamming_distance += 1
        return hamming_distance
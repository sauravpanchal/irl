# sort-integers-by-the-number-of-1-bits

class Solution:
    def countBits(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        hash_map = dict()
        total = 0
        arr.sort()
        for num in arr:
            total = self.countBits(num)
            # string = bin(num)[2:]
            # total = sum(map(int,list(string)))
            if hash_map.get(total):
                hash_map[total].append(num)
            else:
                hash_map[total] = [num]
        result = list()
        for i in range(15):
            if hash_map.get(i): # it returns None if key is not found (or default value if given)
                result += hash_map[i]
        return result
# kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if (candies[i]+extraCandies) >= max(candies) else False for i in range(len(candies))]
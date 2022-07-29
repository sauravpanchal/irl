# count-number-of-teams

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def count_me(arr):
            # function returns number of smaller elements from left to right direction
            l = [0] * len(arr)
            result = 0
            for i in range(len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        # print(arr[i], arr[j])
                        l[i] += 1
                        result += l[j]
                        # print("l",l, "res",result)
            return result
        # we add number smaller by passing original array (L->R) and reversed array (L->R)
        return count_me(rating) + count_me(rating[::-1]) 
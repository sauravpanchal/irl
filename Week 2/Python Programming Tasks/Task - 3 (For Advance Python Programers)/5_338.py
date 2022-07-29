# counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            string = bin(i)[2:]
            l.append(sum(map(int,list(string))))
        return l
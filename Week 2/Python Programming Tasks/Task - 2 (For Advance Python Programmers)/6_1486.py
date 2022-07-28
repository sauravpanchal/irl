# xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        form_list = list()
        xor = 0
        for i in range(n):
            form_list.append((start + 2 * i))
        for i in range(len(form_list)):
            xor ^= form_list[i]
        return xor
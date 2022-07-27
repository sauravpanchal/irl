# defanging-an-ip-address/submissions/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # result = ""
        # for i in address:
        #     if i == ".":
        #         result += "[.]"
        #     else:
        #         result += i
        # return result
        return address.replace(".", "[.]")
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        while columnNumber>0:
            columnNumber -= 1
            res.append(s[columnNumber % 26])
            columnNumber //= 26
        return "".join(reversed(res))
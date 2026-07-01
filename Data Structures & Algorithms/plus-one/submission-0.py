class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        count = len(digits)
        for digit in digits:
            n += digit * (10 ** (count - 1))
            count -= 1
        n += 1
        res = []
        while(n > 0):
            digit = n % 10
            res.append(digit)
            n = n // 10
        res.reverse()
        return res

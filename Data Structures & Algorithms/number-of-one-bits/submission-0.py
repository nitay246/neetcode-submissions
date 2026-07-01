class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = list(n)
        return n.count('1')
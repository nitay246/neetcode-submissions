class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        maxi = res
        for a in nums:
            if a == 0:
                res = 0
            else:
                res += 1
            maxi = max(maxi, res)
        return maxi
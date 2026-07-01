class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        if (int(n*(n + 1))/2) != sum(nums):
            return (int(n*(n + 1)/2)) - sum(nums)
        elif 0 not in nums:
            return 0
        else:
            return n + 1
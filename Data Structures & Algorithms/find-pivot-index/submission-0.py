class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            r = total - l - nums[i]
            if r == l:
                return i
            l += nums[i]
        return -1

        
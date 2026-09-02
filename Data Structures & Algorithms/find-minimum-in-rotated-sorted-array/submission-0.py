class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        if nums[r] > nums[l]:
            return nums[l]
        else:
            mini = nums[r]
            while l <= r:
                k = (l + r) // 2
                if nums[k] < mini:
                    mini = nums[k]
                    r = k
                else:
                    l = k + 1
            return mini
        
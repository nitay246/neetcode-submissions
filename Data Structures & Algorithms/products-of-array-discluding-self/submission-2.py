class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mul *= num

        res = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count > 1:
                res[i] = 0
            elif zero_count == 1:
                res[i] = mul if nums[i] == 0 else 0
            else:
                res[i] = mul // nums[i]

        return res

        
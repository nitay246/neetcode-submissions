class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapi = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapi:
                return [mapi[diff], i]
            mapi[n] = i
        return -1
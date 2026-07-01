class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sety = set()
        for a in nums:
            sety.add(a)
        for a in sety:
            nums.remove(a)
            if a not in nums:
                return a
                
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort fo 2 sum
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            #skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #start 2sum
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            
            while r > l:
                if nums[r] + nums[l] < target:
                    l += 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    #skiping in the pointers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

            
        

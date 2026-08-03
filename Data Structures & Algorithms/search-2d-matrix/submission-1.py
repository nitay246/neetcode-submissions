class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left + ((right-left) // 2)
            if matrix[mid][0] > target:
                right = mid - 1 
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:   
                return self.binarySearch(matrix[mid], target)
        
        return False   
        
        
    def binarySearch(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = l + ((r-l)//2)
            if nums[m]>target:
                r = m-1
            elif nums[m]<target:
                l = m+1
            else:
                return True     
        return False
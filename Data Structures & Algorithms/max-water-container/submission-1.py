class Solution:
    def maxArea(self, heights: List[int]) -> int:       
        r = len(heights) - 1
        l = 0
        res = 0
        while l < r:
            #take the minimum height
            mini = min(heights[l], heights[r])
            #calculate the water based on the position
            pos = r - l
            res  = max(res, pos * mini)
            #move the smaller pointer
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

        
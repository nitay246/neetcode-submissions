class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)
        sum = 0
        while(True):
            if i == 1 or i == 0:
                return sum
            if cost[i-1] >= cost[i-2]:
                sum = sum + cost[i-2]
                i = i - 2
            else:
                sum = sum + cost[i-1]
                i = i - 1
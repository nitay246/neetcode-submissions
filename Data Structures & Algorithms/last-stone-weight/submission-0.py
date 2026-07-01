class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(stones):
            stones.sort()
            slen= len(stones)
            if slen == 1:
                return stones[0]
            res = stones[slen-1]- stones[slen-2]
            if not res:
                stones.remove(stones[slen-1])
                stones.remove(stones[slen-2])
            else:
                stones.remove(stones[slen-1])
                stones[slen-2] = res
        return 0

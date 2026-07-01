class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0 and low % 2 == 0:
            return int((high - low)/2)
        else:
            return 1 + int(math.floor((high - low)/2))

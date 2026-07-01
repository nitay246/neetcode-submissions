class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for a in nums:
            dic[a] += 1
        for i in range(k):
            val = max(dic, key=dic.get)
            res.append(val)
            dic.pop(val, None)
        return res



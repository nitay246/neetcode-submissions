class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = defaultdict(int)
        incoming = defaultdict(int)

        for src, dst in trust:
            out[src] += 1
            incoming[dst] += 1
        for i in range(1, n+1):
            if out[i] == 0 and incoming[i] == n-1:
                return i
        return -1 
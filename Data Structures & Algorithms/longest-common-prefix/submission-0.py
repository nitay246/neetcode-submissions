class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = strs[0]
        for stri in strs:
            if len(stri) < len (short):
                short = stri
        for stri in strs:
            while not stri.startswith(short):
                short = short[:-1]
            if not short:
                return ""
        return short
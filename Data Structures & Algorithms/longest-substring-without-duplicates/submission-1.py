class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        mp = {}
        l = 0
        res = 0

        #the right side of the window always move right
        for r in range(len(s)):
            if s[r] in mp:
                #update the left side of the window
                l = max(mp[s[r]] + 1, l)
            #adding the char to the map with position 
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
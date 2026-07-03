class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False
        #creating 2 0-arrays
        s1count, s2count = [0] * 26, [0] * 26
        #fill the arrays with the number of the appearance of the chars
        for i in range(len1):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        #check matches
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)

        #sliding window part
        l = 0
        for r in range(len1, len2):
            if matches == 26: return True
            #moving the window to the right with r
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            #moving the window to the right with l
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        
        return matches == 26
        


        #note: we can replace the arrays with hashmaps. 
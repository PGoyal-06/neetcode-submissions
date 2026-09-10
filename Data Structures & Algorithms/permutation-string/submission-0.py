class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        c_s1 = {}
        c_s2 = {}

        for char in s1:
            if char in c_s1:
                c_s1[char] += 1
            else:
                c_s1[char] = 1
        
        for r in range(len(s2)):
            if s2[r] in c_s2:
                c_s2[s2[r]] += 1
            else:
                c_s2[s2[r]] = 1

            while (r - l + 1) > len(s1):
                c_s2[s2[l]] -= 1
                if c_s2[s2[l]] == 0:
                    del c_s2[s2[l]]
                l += 1
            
            if c_s1 == c_s2:
                return True
        
        return False
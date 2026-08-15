class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hms1 = {}
        n = len(s1)

        for char in s1:
            hms1[char] = hms1.get(char, 0) + 1

        left = 0
        n = len(s2)
        hms2 = {}
        for right in range(n):
            hms2[s2[right]] = hms2.get(s2[right], 0) + 1
            if right-left+1 > len(s1):
                hms2[s2[left]] -=1
                if hms2[s2[left]] == 0:
                    del hms2[s2[left]]
                left+=1
            
            if hms2 == hms1:
                return True
        return False

        
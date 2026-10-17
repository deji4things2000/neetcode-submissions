class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = {}
        hm2 = {}
        n = len(s2)
        left = 0

        for char in s1:
            hm1[char] = hm1.get(char, 0) + 1
        
        for right in range(n):
            hm2[s2[right]] = hm2.get(s2[right], 0) + 1
            window = right-left+1
            if window > len(s1):
                hm2[s2[left]]-=1
                if hm2[s2[left]] == 0:
                    del hm2[s2[left]]
                left+=1
            if hm2 == hm1:
                return True

        return False



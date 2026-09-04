class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm = {}

        for c in s1:
            hm[c] = hm.get(c, 0) + 1

        n = len(s2)
        left = 0
        hm2 = {}
        for right in range(n):
            hm2[s2[right]] = hm2.get(s2[right], 0) + 1
            
            win = right-left+1
            if win > len(s1):
                hm2[s2[left]] -=1
                if hm2[s2[left]] == 0:
                    del hm2[s2[left]]
                left+=1

            if hm2 == hm:
                return True

        return False


        
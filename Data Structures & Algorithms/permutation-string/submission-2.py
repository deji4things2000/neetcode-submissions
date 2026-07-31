class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        hm1 = {}

        for i in range(n):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1

        k = len(s2)

        for i in range(k): 
            j = i
            hm2 = {}
            while j<k:
                hm2[s2[j]] = hm2.get(s2[j], 0) + 1
                if hm2 == hm1:
                    return True
                j+=1
        return False
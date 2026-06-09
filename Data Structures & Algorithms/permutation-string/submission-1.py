class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hms1 = {}
        n1 = len(s1)

        for i in range(n1):
            hms1[s1[i]] = hms1.get(s1[i], 0) + 1


        n = len(s2)
        for i in range(n):
            j=i
            hm={}
            while j<n:
                hm[s2[j]] = hm.get(s2[j], 0) + 1
                if hms1 == hm:
                    return True
                j+=1
                
        return False




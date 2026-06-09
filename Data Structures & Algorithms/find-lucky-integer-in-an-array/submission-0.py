class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cntD = {}

        for r in arr:
            cntD[r] = cntD.get(r, 0) + 1
        
        maxi = -1
        for key, val in cntD.items():
            if val == key:
                maxi = max(maxi, val)
        return maxi


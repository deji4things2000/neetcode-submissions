class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hs = {}
        maxi = -1

        for e in nums:
            hs[e] = hs.get(e, 0) + 1
        
        for k, v in hs.items():
            if hs[k] == 1:
                maxi = max(maxi, k)
        
        return maxi

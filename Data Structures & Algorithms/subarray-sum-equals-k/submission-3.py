class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = 0
        hm = {0:1}
        count = 0

        for i in range(n):
            ps +=nums[i]
            if ps-k in hm:
                count+=hm[ps-k]
            hm[ps] = hm.get(ps, 0) + 1
        return count
            
        
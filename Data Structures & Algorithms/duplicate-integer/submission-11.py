class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        n = len(nums)

        for i in nums:
            hm[i] = hm.get(i,0) + 1
        
        for v in hm.values():
            if v>1:
                return True
        return False

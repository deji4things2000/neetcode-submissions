class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for v in hm.values():
            if v>1:
                return True
        return False
        
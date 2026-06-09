class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for k,v in hm.items():
            if v>1:
                return True
        return False
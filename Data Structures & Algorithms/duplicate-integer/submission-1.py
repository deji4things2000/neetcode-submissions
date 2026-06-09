class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        ls = len(a)
        l = len(nums)
        if ls!=l:
            return True
        else:
            return False
        

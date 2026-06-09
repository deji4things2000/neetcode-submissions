class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kset = set(nums)

        if len(kset) < len(nums):
            return True
        else:
            return False
            

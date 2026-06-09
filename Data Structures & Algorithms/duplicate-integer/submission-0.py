class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=nums
        ds = set(nums)
        if len(ds) == len(nums):
            return False
        else:
            return True
        
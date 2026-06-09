class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        app=set(nums)
        return len(app)<len(nums)

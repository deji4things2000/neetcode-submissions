class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain = set(nums)
        return len(contain) != len(nums)
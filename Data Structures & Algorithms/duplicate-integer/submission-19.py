class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)
        return len(nums) != len(nset)
        
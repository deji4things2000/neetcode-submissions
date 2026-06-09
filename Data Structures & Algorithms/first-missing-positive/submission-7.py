class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        nset = set(nums)

        while i in nset:
            i+=1
        return i
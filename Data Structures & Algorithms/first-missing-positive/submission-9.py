class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nset = set(nums)
        i = 1

        while i in nset:
            i+=1
        return i
        
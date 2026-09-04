class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        k = 1

        while k in seen:
            k+=1
        return k
        
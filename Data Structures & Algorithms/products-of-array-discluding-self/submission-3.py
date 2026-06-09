class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pf = 1
        for i in range(len(nums)):
            res[i] = pf
            pf*=nums[i]
        pst = 1
        for i in reversed(range(len(nums))):
            res[i] *= pst
            pst*=nums[i]
        return res

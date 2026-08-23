class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        minV, maxV, res = nums[0], nums[0], nums[0]

        for i in range(1, n):
            cand = (nums[i], minV*nums[i], maxV*nums[i])
            maxV = max(cand)
            minV = min(cand)
            res = max(res, maxV)
        return res

        
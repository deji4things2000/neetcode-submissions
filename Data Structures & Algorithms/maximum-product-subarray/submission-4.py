class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        maxi = nums[0]
        mini = nums[0]
        res = nums[0]

        for i in range(1, n):
            cand = (nums[i], maxi*nums[i], mini*nums[i])
            maxi = max(cand)
            mini = min(cand)
            res = max(res, maxi)
        return res
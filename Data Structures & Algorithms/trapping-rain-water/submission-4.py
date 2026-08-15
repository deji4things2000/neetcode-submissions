class Solution:
    def trap(self, height: List[int]) -> int:
        nums = height
        n = len(nums)
        i, j = 0, n-1
        maxL = nums[i]
        maxR = nums[j]
        res = 0

        while i<j:
            if maxL <= maxR:
                i+=1
                maxL = max(maxL, nums[i])
                res += maxL - nums[i]
            else:
                j-=1
                maxR = max(maxR, nums[j])
                res += maxR - nums[j]
        return res



        
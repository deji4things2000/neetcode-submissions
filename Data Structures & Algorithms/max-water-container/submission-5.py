class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        n = len(nums)
        i, j = 0, n-1
        maxi = 0

        while i<j:
            h = min(nums[i], nums[j])
            w = j-i
            area = h*w
            maxi = max(maxi, area)

            if nums[i] <= nums[j]:
                i+=1
            else:
                j-=1
        return maxi

        
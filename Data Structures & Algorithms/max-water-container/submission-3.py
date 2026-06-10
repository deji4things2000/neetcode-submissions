class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        n = len(heights)
        i, j = 0, n-1
        maxi = 0

        while i<j:
            width = j-i
            height = min(nums[i], nums[j])
            area = height * width
            maxi = max(maxi, area)
            
            if nums[i] < nums[j]:
                i+=1
            elif nums[i] >= nums[j]:
                j-=1
        return maxi

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        maxi = 0

        while i<j:
            width = j-i
            height = min(heights[i], heights[j])
            area = height * width
            maxi = max(maxi, area)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxi

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxi = 0

        while i<j:
            w = (j-i)
            h = min(heights[j],  heights[i])

            area = w*h
            maxi = max(maxi, area)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxi

        
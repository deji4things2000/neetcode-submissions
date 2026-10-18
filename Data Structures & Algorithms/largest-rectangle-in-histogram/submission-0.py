class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxi = 0
        heights.append(0)
        n = len(heights)

        for i in range(n):

            while s and heights[i] < heights[s[-1]]:
                h = heights[s.pop()]

                if not s:
                    width = i
                else:
                    width = i - s[-1] - 1

                area = h * width
                maxi = max(maxi, area)
            s.append(i)
        heights.pop()
        return maxi


        
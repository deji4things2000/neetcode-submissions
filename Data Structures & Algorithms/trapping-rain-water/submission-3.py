class Solution:
    def trap(self, height: List[int]) -> int:
        maxi = 0
        i, j = 0, len(height)-1
        maxL, maxR = height[i], height[j]

        while i<j:
            if maxL <= maxR:
                i+=1
                maxL = max(maxL, height[i])
                maxi += maxL - height[i]
            else:
                j-=1
                maxR = max(maxR, height[j])
                maxi += maxR - height[j]
        return maxi

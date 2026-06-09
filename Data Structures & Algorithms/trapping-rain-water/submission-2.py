class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0, n-1

        maxL, maxR = height[i], height[j]

        res = 0

        while i<j:
            if maxL < maxR:
                i+=1
                maxL=max(maxL, height[i])
                res+=maxL-height[i]
            else:
                j-=1
                maxR = max(maxR, height[j])
                res+=maxR-height[j]
        return res


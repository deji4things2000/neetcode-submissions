class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        if n==1:
            return nums[0]

        maxV = minV = result = nums[0]

        for num in nums[1:]:
            cand = (num, maxV*num, minV*num)
            maxV = max(cand)
            minV = min(cand)
            result = max(result, maxV)
        
        return result

        
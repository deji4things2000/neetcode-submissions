class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            val = nums[i] * nums[i]
            res.append(val)
        res.sort()
        return res


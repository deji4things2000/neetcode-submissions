class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0

        for n in nums:
            cnt += 1 if n else -cnt
            res = max(res, cnt)
        return res
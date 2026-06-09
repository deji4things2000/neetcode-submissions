class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmp:
                return [hmp[diff], i]
            hmp[n] = i
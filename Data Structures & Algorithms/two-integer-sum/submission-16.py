class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            hm[nums[i]] = i




              


        
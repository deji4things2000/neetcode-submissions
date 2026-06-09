class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rs = 0
        ls = 0
        total = sum(nums)


        for i in range(len(nums)):
            rs = total - ls - nums[i]
            if rs == ls:
                return i
            ls+=nums[i]
        return -1






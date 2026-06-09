class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hm = {}
        n = len(nums)

        for i in range(n):
            hm[nums[i]] = hm.get(nums[i], 0) + 1

        for k,v in hm.items():
            if v > 1:
                return True
        return False
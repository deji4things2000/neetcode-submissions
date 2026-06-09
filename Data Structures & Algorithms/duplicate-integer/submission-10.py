class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        for value in hm.values():
            if value>1:
                return True
            else:
                continue
        return False

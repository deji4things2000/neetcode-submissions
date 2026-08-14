class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hm = {}

        for i in range(n):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        for k,v in hm.items():
            if v > (n//2):
                return k
        
        
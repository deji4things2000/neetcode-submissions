class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for k, v in hm.items():
            if v > (n//2):
                return k
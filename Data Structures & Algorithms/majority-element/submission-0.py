class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntS = {}
        n=len(nums)

        for num in nums:
            cntS[num] = 1 + cntS.get(num, 0)

        for key, val in cntS.items():
            if val > n//2:
                return key
        
        
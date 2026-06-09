class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []
        n = len(nums)

        for num in nums:
            hm[num] = hm.get(num,0) + 1
        
        for k, v in hm.items():
            if (v>n//3):
                res.append(k)
        return res
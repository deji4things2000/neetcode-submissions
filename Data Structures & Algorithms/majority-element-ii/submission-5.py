class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        res = []
        for k,v in hm.items():
            if v > (n//3):
                res.append(k)
        return res

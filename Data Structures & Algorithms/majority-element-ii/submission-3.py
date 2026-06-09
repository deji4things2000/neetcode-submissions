class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        n =  len(nums)

        for i in range(n):
            hm[nums[i]] = hm.get(nums[i],0) + 1
        
        res = []
        
        for k,v in hm.items():
            if v>n//3:
                res.append(k)
        return res
        
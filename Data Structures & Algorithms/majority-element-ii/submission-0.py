class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []

        for v in nums:
            hm[v] = hm.get(v,0) + 1

        for k, cnt in hm.items():
            if cnt > len(nums)//3:
                res.append(k)
        
        return res
        
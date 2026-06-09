class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0) +1
        
        for k, v in hm.items():
            if v ==1:
                return k
        
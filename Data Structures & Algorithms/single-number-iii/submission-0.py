class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0) + 1
        res = []
        for k, v in hm.items():
            if v == 1:
                res.append(k)

        return res
        
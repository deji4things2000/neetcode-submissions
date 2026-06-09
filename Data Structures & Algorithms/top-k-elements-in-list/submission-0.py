class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []

        for num in nums:
            hm[num] = 1+hm.get(num,0)
        
        for i in range(0, k):
            max_key = max(hm, key=hm.get)
            res.append(max_key)
            rm = hm.pop(max_key)
        return res




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hm = {}

        for i in range(n):
            hm[nums[i]] = hm.get(nums[i], 0) + 1

        
        sortH = sorted(hm.items(), key = lambda x: x[1], reverse = True) [:k]

        res = []
        for k,v in sortH:
            res.append(k)
        return res
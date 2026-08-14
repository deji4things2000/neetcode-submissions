class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        n = len(nums)

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        sortedh = sorted(hm.items(), key = lambda a: a[1], reverse = True) [:k]

        res = []

        for k, v in sortedh:
            res.append(k)
        return res
        
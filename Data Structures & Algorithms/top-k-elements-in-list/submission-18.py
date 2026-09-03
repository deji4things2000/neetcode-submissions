class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        sortedhm = sorted(hm.items(), key = lambda a: a[1], reverse = True)[:k]

        res = []

        for k,v in sortedhm:
            res.append(k)
        return res
        
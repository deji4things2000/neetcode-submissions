class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1


        sorthm = sorted(hm.items(), key = lambda a: a[1], reverse = True)[:k]


        res = []
        for a,b in sorthm:
            res.append(a)
        return res

        
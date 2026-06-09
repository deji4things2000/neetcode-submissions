class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm =  {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        sorted_array =  sorted(hm.items(), key = lambda x:x[1], reverse = True)[:k]

        res = []

        for k,v in sorted_array:
            res.append(k)

        return res


        
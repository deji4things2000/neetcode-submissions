class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        sorthm = sorted(hm.items(), key = lambda x:x[1], reverse = True )[:k]

        res=[]

        for ky,v in sorthm:
            res.append(ky)
        return res

        






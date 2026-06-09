from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {} 
        #hm = Counter(nums)
        res = []

        #comment this out if using the Counter function
        for num in nums:
            hm[num] = 1+hm.get(num,0)
        
        for i in range(0, k):
            max_key = max(hm, key=hm.get)
            res.append(max_key)
            hm.pop(max_key)
        return res




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1

        
        shm = sorted(hm.items(), key = lambda x: x[1], reverse = True) [:k]

        res = [k for k, v in shm]
        
        return res
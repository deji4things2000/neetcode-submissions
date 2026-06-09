class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        n = len(nums)
        
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        shm = sorted(hm.items(), key = lambda x:x[0])
        
        res = []

        for k,v in shm:
            if v>(n/3):
                res.append(k)
        return res
        
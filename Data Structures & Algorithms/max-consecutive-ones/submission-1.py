class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        store = 0

        for i in nums:
            if i == 1:
                cnt+=1
                store = max(cnt, store)
            else:
                cnt=0
        return store
            
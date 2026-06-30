class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        n = len(nums)
        count = 0
        maxi = 0

        for num in nums:
            new = num
            count =1
            while num+1 in ss:
                count+=1
                num+=1
            maxi = max(maxi, count)
        return maxi
            


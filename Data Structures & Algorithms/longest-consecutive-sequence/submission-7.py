class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        dd = set(nums)
        maxi = 0


        for i in range(n):
            new = nums[i]
            l=1
            while (new+1) in dd:
                l+=1
                new+=1
            maxi = max(maxi, l)
        return maxi
            
            
            
        
        
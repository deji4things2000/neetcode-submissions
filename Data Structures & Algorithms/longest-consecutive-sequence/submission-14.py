class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        maxi = 0

        for num in nums:
            if num-1 not in seen:
                new = num
                count = 1

                while (new+1) in seen:
                    count+=1
                    new+=1
                maxi = max(maxi, count)
        return maxi

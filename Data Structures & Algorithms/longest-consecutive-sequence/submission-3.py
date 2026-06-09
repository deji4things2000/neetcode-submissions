class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        res=0
        for num in ns:
            if (num-1) not in ns:
                lenght =1
                while (num+lenght) in ns:
                    lenght+=1
                res=max(lenght, res)
        return res

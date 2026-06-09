class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        long = 0
        for num in ns:
            if (num-1) not in ns:
                lens = 1
                while (num+lens) in ns:
                    lens+=1
                long = max(long, lens)
        return long


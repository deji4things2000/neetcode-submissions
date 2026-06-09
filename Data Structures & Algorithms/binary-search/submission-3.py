class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo<=hi:
            if nums[lo] == target:
                return lo
            elif nums[hi] == target:
                return hi
            lo+=1
            hi-=1
        return -1
            

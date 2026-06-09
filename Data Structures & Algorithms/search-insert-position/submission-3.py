class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n-1

        while lo<=hi:
            mid = (lo+hi)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo+=1
            else:
                hi-=1
            
        return lo
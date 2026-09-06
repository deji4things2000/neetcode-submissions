class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n-1

        while i<j:
            mid = (i+j)//2

            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid
        return nums[i]


        
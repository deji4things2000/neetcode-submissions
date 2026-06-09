class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):

            if len(nums)<=1:
                return nums
            
            pivot = nums[len(nums)//2]

            left = []
            middle = []
            right = []

            for c in nums:
                if c<pivot:
                    left.append(c)
                elif c>pivot:
                    right.append(c)
                else:
                    middle.append(c)
            
            return quicksort(left)+middle+quicksort(right)
        
        return quicksort(nums)



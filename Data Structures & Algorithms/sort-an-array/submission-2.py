class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            
            # Choose pivot
            pivot = nums[len(nums) // 2]  # middle element

            left = []
            middle = []
            right = []

            # Partition list
            for element in nums:
                if element < pivot:
                    left.append(element)
                elif element == pivot:
                    middle.append(element)
                else:
                    right.append(element)
            
            # Recursively sort left and right
            return quicksort(left) + middle + quicksort(right)

        return quicksort(nums)




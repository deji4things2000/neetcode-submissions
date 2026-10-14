class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(num, left, right):
            if left >=right:
                return

            mid = (left+right)//2
            nums[mid], nums[left] = nums[left], nums[mid]

            l = left
            r = left+1

            while r<=right:
                if num[r] < nums[left]:
                    l+=1
                    nums[r], nums[l] = nums[l], nums[r]
                r+=1
            nums[l], nums[left] = nums[left], nums[l]
            quicksort(num, left, l-1)
            quicksort(num, l+1, right)
        
        quicksort(nums, 0, len(nums)-1)
        return nums



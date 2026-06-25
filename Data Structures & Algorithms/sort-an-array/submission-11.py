class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(left, right):
            if left>=right:
                return

            mid = (left+right)//2
            nums[left], nums[mid] = nums[mid], nums[left]
            pivot = nums[left]

            lt = left
            i = left+1
            gt = right

            while i<=gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt+=1
                    i+=1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt-=1
                else:
                    i+=1
            quicksort(left, lt-1)
            quicksort(gt+1, right)
        quicksort(0, len(nums)-1)
        return nums


        
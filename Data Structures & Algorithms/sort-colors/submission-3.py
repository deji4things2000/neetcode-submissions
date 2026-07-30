class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(arr, left, right):
            if left>=right:
                return

            mid = (left+right)//2
            arr[mid], arr[left] = arr[left], arr[mid]

            l = left
            r = left+1

            while r<=right:
                if arr[r] < arr[left]:
                    l+=1
                    arr[l], arr[r] = arr[r], arr[l]
                r+=1
            arr[left], arr[l] = arr[l], arr[left]

            quicksort(arr, left, l-1)
            quicksort(arr, l+1, right)
        
        quicksort(nums, 0, len(nums)-1)
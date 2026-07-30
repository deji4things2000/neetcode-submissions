class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

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
                    arr[r], arr[l] = arr[l], arr[r]
                r+=1
            arr[l], arr[left] = arr[left], arr[l]
            quicksort(arr, left, l-1)
            quicksort(arr, l+1, right)
        
        quicksort(nums, 0, len(nums)-1)
        return nums
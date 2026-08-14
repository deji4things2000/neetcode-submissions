class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(num, left, right):
            if left>=right:
                return
            
            mid = (left+right)//2
            num[mid], num[left] = num[left], num[mid]

            l = left
            r = left + 1
            while r<=right:
                if num[r] < num[left]:
                    l+=1
                    num[r], num[l] = num[l], num[r]
                r+=1
            num[l], num[left] = num[left], num[l]

            quicksort(num, left, l-1)
            quicksort(num, l+1, right)
        
        quicksort(nums, 0, len(nums)-1)
        
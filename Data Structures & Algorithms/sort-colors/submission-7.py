class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def qs(num, left, right):
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
            qs(num, left, l-1)
            qs(num, l+1, right)
        
        qs(nums, 0, len(nums)-1)

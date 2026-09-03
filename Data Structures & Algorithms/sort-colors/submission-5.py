class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick(num, left, right):
            if left>=right:
                return

            mid = (left+right)//2
            num[left], num[mid] = num[mid], num[left]

            l = left
            r = left + 1

            while r<=right:
                if num[r] < num[left]:
                    l+=1
                    num[l], num[r] = num[r], num[l]
                r+=1
            num[l], num[left] = num[left], num[l]

            quick(num, left, l-1)
            quick(num, l+1, right)
        quick(nums, 0, len(nums)-1)
        return nums